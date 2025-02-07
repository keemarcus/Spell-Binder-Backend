Set_User_ID()

async function Set_User_ID(){
    // use fetch to get the id of the current user
    let url = "http://localhost:5000/session/user_id"
    let response = await fetch(url)
    let user_id = await response.text()

    var input = document.createElement("input");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", "user_id");
    input.setAttribute("value", user_id);
    document.getElementById("new_spell").appendChild(input);
}
