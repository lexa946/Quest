const host = document.location.host;

class Hero {
    constructor() {
        this.id = $('#hero_pk').text();
        this.name = $('#hero_name').text();
        const skill = document.querySelector('#hero_skill')
        const stamina = document.querySelector('#hero_stamina')
        const luck = document.querySelector('#hero_luck')
        const provision = document.querySelector('#hero_provisions')
        const money = document.querySelector('#hero_money')

        this._currentSkill = parseInt(skill.querySelectorAll('span')[0].textContent)
        this.maxSkill = parseInt(skill.querySelectorAll('span')[1].textContent)

        this._currentStamina = parseInt(stamina.querySelectorAll('span')[0].textContent)
        this.maxStamina = parseInt(stamina.querySelectorAll('span')[1].textContent)

        this._currentLuck = parseInt(luck.querySelectorAll('span')[0].textContent)
        this.maxLuck = parseInt(luck.querySelectorAll('span')[1].textContent)

        this._provision = parseInt(provision.textContent)
        this.money = parseInt(money.textContent)

    }

    refreshCharacteristic() {
        $('#hero_skill span:first-child').text(this.currentSkill)
        $('#hero_skill span:last-child').text(this.maxSkill)

        $('#hero_stamina span:first-child').text(this.currentStamina)
        $('#hero_stamina span:last-child').text(this.maxStamina)

        $('#hero_luck span:first-child').text(this.currentLuck)
        $('#hero_luck span:last-child').text(this.maxLuck)

        $('#hero_provisions').text(this.provision)
        $('#hero_money').text(this.money)

        const json = JSON.stringify(this);
        console.log(json)
        let request = new XMLHttpRequest();
        request.open("POST", 'http://' + host + '/api/hero/characteristic/?pk=' + this.id);
        request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
        request.send(json);
    }

    async getInventory() {
        let items = []
        let response = await fetch('http://' + host + '/api/hero/inventory?pk=' + this.id)
        const answer = await response.json()
        $.each(answer, (key, value) => {
            items.push(value)
        })
        return items
    }

    async getBuffs() {
        let items = []
        let response = await fetch('http://' + host + '/api/hero/buffs?pk=' + this.id)
        const answer = await response.json()
        $.each(answer, (key, value) => {
            items.push(value)
        })
        return items
    }


    get currentSkill() {
        return this._currentSkill
    }

    set currentSkill(value) {
        if (value > this.maxSkill) value = this.maxSkill;
        if (value <= 0) value = 0;
        this._currentSkill = value
    }

    get currentStamina() {
        return this._currentStamina
    }

    set currentStamina(value) {
        if (value > this.maxStamina) value = this.maxStamina;
        if (value <= 0) value = 0;
        this._currentStamina = value
    }

    get currentLuck() {
        return this._currentLuck
    }

    set currentLuck(value) {
        if (value > this.maxLuck) value = this.maxLuck;
        if (value <= 0) value = 0;
        this._currentLuck = value
    }

    get provision() {
        return this._provision
    }

    set provision(value) {
        if (value <= 0) value = 0;
        this._provision = value
    }

}

class Enemy {
    constructor(name, skill, stamina) {
        this.name = name
        this.skill = skill
        this._stamina = stamina
    }

    refreshCharacteristic() {
        const selector = 'tr:contains("' + this.name + '")'
        const enemyRow = $(selector)
        enemyRow.find("td:nth-child(2)").text(this.skill)
        enemyRow.find("td:nth-child(3)").text(this.stamina)
    }


    get stamina() {
        return this._stamina
    }

    set stamina(value) {
        if (value <= 0) value = 0;
        this._stamina = value
    }
}


function getEnemies() {
    let enemies = []

    $('.enemy-row').each(function () {
        const characteristics = this.querySelectorAll('td')
        const name = characteristics[0].textContent
        const skill = +characteristics[1].textContent
        const stamina = +characteristics[2].textContent
        let enemy = new Enemy(name, skill, stamina)
        enemies.push(enemy)
    })
    return enemies
}


function getRandomInt(min, max) {
    return Math.floor(min + Math.random() * (max + 1 - min))
}


const hero = new Hero()

const provisionButton = $("#provision_btn")

if (hero.currentStamina === hero.maxStamina || hero.provision === 0) {
    provisionButton.attr('disabled', 'disabled')
}

provisionButton.bind("click", function (event) {
    hero.provision--
    hero.currentStamina += 4;
    if (hero.currentStamina === hero.maxStamina || hero.provision === 0) {
        provisionButton.attr('disabled', 'disabled')
    }

    hero.refreshCharacteristic()

})

if ($('div').is('#enemies')) {
    provisionButton.attr('disabled', 'disabled')

    let enemies = getEnemies()

    let btnContinue = $('.btn.btn-info:first-child')
    btnContinue.addClass('disabled')


    let btnPunch = document.querySelector('#punch')


    btnPunch.onclick = function (event) {
        let currentEnemy = enemies[0].stamina <= 0 ? enemies[1] : enemies[0];

        btnPunch.setAttribute('disabled', 'disabled')
        let fightHistory = $('.history-fight div.content')

        let enemyRoll = getRandomInt(1, 12) + enemies[0].skill
        let heroRoll = getRandomInt(1, 12) + hero.currentSkill


        if (enemyRoll > heroRoll) {
            hero.currentStamina -= 2
            fightHistory.append($('<div>', {'text': 'Противник нанес тебе ранение'}))

        } else if (enemyRoll === heroRoll) {
            fightHistory.append($('<div>', {'text': 'Вы отразили удары друг друга'}))

        } else if (enemyRoll < heroRoll) {
            currentEnemy.stamina -= 2
            fightHistory.append($('<div>', {'text': 'Ты нанес ранение противнику'}))
        }

        if (enemies.length > 1) {
            if (enemies[0].stamina > 0 || enemies[1].stamina > 0) {
                btnPunch.removeAttribute('disabled')
            } else if (enemies[0].stamina <= 0 && enemies[1].stamina <= 0) {
                btnContinue.removeClass('disabled')
                fightHistory.append($('<div>', {'text': '!Вы победили!'}))
            }
        } else {
            if (currentEnemy.stamina > 0) {
                btnPunch.removeAttribute('disabled')
            } else if (currentEnemy.stamina <= 0) {
                btnContinue.removeClass('disabled')
                fightHistory.append($('<div>', {'text': '!Вы победили!'}))
            }
        }


        currentEnemy.refreshCharacteristic()
        hero.refreshCharacteristic()
        fightHistory.scrollTop(fightHistory.height())
    }
}


function tryYourLuck() {
    let btnsContinue = $('#ways a')
    btnsContinue.each(function () {
        $(this).addClass('disabled')
    })

    let roll = getRandomInt(1, 12)
    console.log(roll)

    if (roll <= hero.currentLuck) {
        btnsContinue[0].classList.remove('disabled')
    } else {
        btnsContinue[1].classList.remove('disabled')
    }

    hero.currentLuck--
    hero.refreshCharacteristic()
}

function tryYourSkill() {
    let btnsContinue = $('#ways a')
    btnsContinue.each(function () {
        $(this).addClass('disabled')
    })

    let roll = getRandomInt(1, 12)
    console.log(roll)

    if (roll <= hero.currentSkill) {
        btnsContinue[0].classList.remove('disabled')
    } else {
        btnsContinue[1].classList.remove('disabled')
    }
}

function haveStuff(stuffName) {

    $('#ways a:first-child').addClass('disabled')

    hero.getInventory().then(function (items) {
        for (let item of items) {
            if (item === stuffName) {
                $('#ways a:first-child').removeClass('disabled')
                $('#ways a:last-child').addClass('disabled')
            }
        }
    })
}
function haveBuff(buffName) {

    $('#ways a:first-child').addClass('disabled')

    hero.getBuffs().then(function (items) {
        for (let item of items) {
            if (item === buffName) {
                $('#ways a:first-child').removeClass('disabled')
                $('#ways a:last-child').addClass('disabled')
            }
        }
    })
}



//Отслеживаем изменение текущей Выносливости
//Если она 0 - игрок погиб
let currentStaminaTag = $('#hero_stamina span:first-child')
currentStaminaTag.bind('DOMSubtreeModified', function (event) {

    if (hero.currentStamina === 0) {
        $('#punch').attr('disabled', 'disabled')
        $('#ways a').each(function () {
            $(this).remove()
        })
        $('#ways').append($('<a>', {
            'href': '/gameover',
            'text': 'Вы погибли!',
            'class': 'btn btn-info',
        }))
    }
})
if (hero.currentStamina === 0) {
    document.location.href = "http://" + host + "/gameover";
}

function arrayRandElement(arr) {
    let rand = Math.floor(Math.random() * arr.length);
    return arr[rand];
}