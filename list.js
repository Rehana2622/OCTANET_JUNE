const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

function addTask() {
    if (inputBox.value.trim() === '') {
        alert("You must write something!");
    } else {
        let li = document.createElement("li");
        li.textContent = inputBox.value;
        let span = document.createElement("span");
        span.textContent = "\u00D7";
        li.appendChild(span);
        listContainer.appendChild(li);
        inputBox.value = "";
        saveData();
    }
}

listContainer.addEventListener("click", function(e) {
    if (e.target.tagName === "LI") {
        e.target.classList.toggle("checked");
        saveData();
    } else if (e.target.tagName === "SPAN") {
        e.target.parentElement.remove();
        saveData();
    }
});

function saveData() {
    localStorage.setItem("tasks", listContainer.innerHTML);
}

function showTasks() {
    listContainer.innerHTML = localStorage.getItem("tasks");
}

showTasks();
