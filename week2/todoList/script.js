const list = [];

function doTask (){
    let element = document.getElementById("typer");
    if(element.value == ""){
        alert("Type something to add");
    }else{
        let div = document.createElement('div');
        list.push(div);
        div.className = "task " + list.length;
        
        let checkbox = document.createElement('input');
        checkbox.setAttribute("type","checkbox");
        checkbox.className = "check " + list.length;
        checkbox.setAttribute("onclick",`checkText(${checkbox.className.split(' ')[1]})`);

        let taskText = document.createElement('div');
        taskText.className = "task_text " + list.length;
        taskText.textContent = element.value;

        checkText = (className) => {
            let checkbox = document.body.getElementsByClassName("check " + className)[0];
            if(checkbox.checked == true){
                document.body.getElementsByClassName("task_text " + className)[0].setAttribute("style","text-decoration: line-through;");
            }
            else{
                document.body.getElementsByClassName("task_text " + className)[0].setAttribute("style","text-decoration: none;");
            }
        }
        
        deleteText = (className) => {
            document.body.removeChild(document.body.getElementsByClassName("task " + className)[0]);
        }
        let img = document.createElement('img');
        img.src = "img/trash1.png";
        img.className = "trash " + list.length;
        img.setAttribute("onclick",`deleteText(${ img.className.split(' ')[1] })`);

        div.appendChild(checkbox);
        div.appendChild(taskText);
        div.appendChild(img);
        document.body.appendChild(div);
        element.value = "";
    }
}