var prepared_spells
set_up_page()

async function set_up_page() {
    prepared_spells = new Set()

    // use fetch to get the id of the current spellbook
    let url = "http://localhost:5000/session/spellbook_id"
    let response = await fetch(url)
    spellbook_id = await response.text()

    // use fetch to get the id of the current user
    url = "http://localhost:5000/session/user_id"
    response = await fetch(url)
    user_id = await response.text()

    if (spellbook_id === 'None') {
        console.log("No spellbook id found")
    } else {
        // use fetch to get the spell stats
        let url = "http://localhost:5000/spellbooks/" + spellbook_id
        let response = await fetch(url)
        character_stats = await response.json()

        // use fetch to get the number of spells and cantrips known
        url = "https://www.dnd5eapi.co/api/classes/" + character_stats["spell_casting_class"] + "/levels/" + character_stats["spell_casting_level"]
        response = await fetch(url)
        class_level_info = await response.json()

        let stats_table = document.getElementById('spell stats')
        // create new table row
        let row = stats_table.insertRow(-1)
        let character_cell = row.insertCell(0)
        let class_cell = row.insertCell(1)
        let level_cell = row.insertCell(2)
        let spells_known_cell = row.insertCell(3)
        let cantrips_known_cell = row.insertCell(4)

        // insert the data into the new row
        character_cell.innerText = character_stats["character_id"].toString().split('-')[1]
        class_cell.innerText = character_stats["spell_casting_class"].charAt(0).toUpperCase() + character_stats["spell_casting_class"].substring(1)
        level_cell.innerText = character_stats["spell_casting_level"]
        if (class_level_info["spellcasting"]["spells_known"]) {
            spells_known_cell.innerText = class_level_info["spellcasting"]["spells_known"]
        } else {
            // handle this later
            // set a limit to the number of spells we can add to the spellbook
        }
        if (class_level_info["spellcasting"]["cantrips_known"]) {
            cantrips_known_cell.innerText = class_level_info["spellcasting"]["cantrips_known"]
        } else {
            // handle this later
            // set a limit to the number of cantrips we can add to the spellbook
        }

        let spell_slot_levels = new Set()
        set_up_spell_slots(character_stats["spell_casting_class"], spell_slot_levels)
        
        // use fetch to get the spells in the current spellbook
        url = "http://localhost:5000/spellbooks/spells/" + spellbook_id
        response = await fetch(url)
        spells = await response.text()
        const spell_list = spells.toString().split(",")
        if(spell_list[0] != ''){
            let table = document.getElementById('current spells table')
            console.log("known spells")
            for (spelll in spell_list){
            // get the full spell info
            let url = "http://localhost:5000/spells/" + spell_list[spelll]
            let response = await fetch(url)
            spell_info = await response.json()
            if(!spell_info["desc"]){break}

            add_known_spell(spell_info, table, character_stats["spell_casting_class"])
        }
        }
        
        // use fetch to get the spells already in the current spellbook
        // url = "http://localhost:5000/spellbooks/spells/" + spellbook_id
        // response = await fetch(url)
        // spells = await response.text()
        // const spell_list = spells.toString().split(",")
        // let table = document.getElementById('current spells table')
        // for (spelll in spell_list) {
        //     // get the full spell info
        //     let url = "http://localhost:5000/spells/" + spell_list[spelll]
        //     let response = await fetch(url)
        //     spell_info = await response.json()
        //     if(!spell_info["desc"]){break}

        //     add_known_spell(spell_info, table, character_stats["spell_casting_class"])
        // }

        console.log("add spell")
        get_spells(character_stats["spell_casting_class"], user_id, character_stats["spell_slot_level"])
    }
}

async function set_up_spell_slots(spell_casting_class){
    // use fetch to get the spell slots
    let url = "http://localhost:5000/spellbooks/slots/" + spellbook_id
    let response = await fetch(url)
    let spell_slots = await response.json()

    let slot_level_row = document.getElementById('slot level row')
    let total_slots_row = document.getElementById('total slots row')

    if(spell_casting_class == "warlock"){
        i = parseInt(Object.keys(spell_slots)[0].split('_')[0])
        // create new table row
        let slot_level_cell = document.createElement("th")
        slot_level_row.appendChild(slot_level_cell)
        let slots_total_cell = total_slots_row.insertCell(-1)

        // insert the data into the new row
        slot_level_cell.innerText = i
        slots_total_cell.innerText = spell_slots[i.toString() + "_total"]

        character_stats["spell_slot_level"] = i
    }else{
        for(let i = 1; i <= (Object.keys(spell_slots).length / 2); i++) {
            // create new table row
            let slot_level_cell = document.createElement("th")
            slot_level_row.appendChild(slot_level_cell)
            let slots_total_cell = total_slots_row.insertCell(-1)
    
            // insert the data into the new row
            slot_level_cell.innerText = i
            slots_total_cell.innerText = spell_slots[i.toString() + "_total"]
            
            character_stats["spell_slot_level"] = i
        }
    }
}

async function get_spells(class_name, user_id, level){
    let add_table = document.getElementById('available spells table')
    //let ctr = 0

    // use fetch to get all the spells available for the class
    let url = "http://localhost:5000/spells/user/" + user_id + "/class/" + class_name + "/level/" + level
    let response = await fetch(url)
    console.log(response)
    all_spells = await response.json()

    for (spell in all_spells) {
        // ctr ++
        // console.log(all_spells[spell])
        // console.log(ctr)
        if (prepared_spells.has(all_spells[spell]["name"])) {
            //console.log("already know")
            continue
        }

        // create new table row
        let row = add_table.insertRow(-1)
        let name_cell = row.insertCell(0)
        let level_cell = row.insertCell(1)
        let remove_cell = row.insertCell(2)

        // insert the data into the new row
        name_cell.innerText = all_spells[spell]["name"]
        if (all_spells[spell]["level"] == 0) {
            level_cell.innerText = "Cantrip"
        } else {
            level_cell.innerText = all_spells[spell]["level"]
        }

        // add the button to add the spell t0 the spellbook
        var btn = document.createElement('input')
        btn.type = "button"
        btn.value = "Add"
        btn.setAttribute('onclick', 'javascript: add_spell(' + spellbook_id + ', "' + all_spells[spell]["index"] + '");');
        remove_cell.appendChild(btn)
    }
}

function remove_spell(spellbook_id, spell_index) {
    const request = new XMLHttpRequest();
    request.open("DELETE", "http://localhost:5000/spellbooks/" + spellbook_id + "/" + spell_index);
    request.send(null);

    location.reload()
}

function add_spell(spellbook_id, spell_index) {
    const request = new XMLHttpRequest();
    request.open("POST", "http://localhost:5000/spellbooks/" + spellbook_id + "/" + spell_index);
    request.send(null);

    location.reload()
}

function add_known_spell(spell_info, table, spell_casting_class){
    // create new table row
    console.log(table)
    let row = table.insertRow(-1)
    let name_cell = row.insertCell(0)
    let level_cell = row.insertCell(1)
    let remove_cell = row.insertCell(2)

    // insert the data into the new row
    name_cell.innerText = spell_info["name"]
    if(spell_info["level"] == 0){
        level_cell.innerText = "Cantrip"
    }else{
        level_cell.innerText = spell_info["level"]
    }
    
    if(spell_info["higher_level"]){
        level_cell.innerText += "+"
    }
    // add the button to remove the spell from the spellbook
    var btn = document.createElement('input')
    btn.type = "button"
    btn.value = "Remove"
    btn.setAttribute('onclick', 'javascript: remove_spell(' + spellbook_id + ', "' + spell_info["index"] + '");');
    remove_cell.appendChild(btn)

    prepared_spells.add(spell_info["name"])
}