
/** active le clic sur le titre pour afficher ou masquer le détail */
const initTaskItem = function (taskItem) {
    const titre = taskItem.querySelector("h3");
    titre.addEventListener("click", function () {
        taskItem.classList.toggle("expanded");
    });

    /** classList manipule les classes CSS
     * toggle() veut dire: si la classe existe,elle est supprimer, 
     * sinon elle est rajouter
     * ici toggle est de la bibliotheque classliste
     */
};

/** une fonction qui ajoute les taches  */
const add_tasks = function(){
    const name = document.getElementsByTagName("input")[0];
    const tasks = document.getElementsByClassName("tache")[0];
    const textarea = document.getElementsByClassName("taskinput")[0];
    const taskBlock = document.createElement("div");
    taskBlock.className = "task-item";
    const sup = document.createElement("button");
    const mod = document.createElement("button");
    sup.textContent = "Supprimer"
    sup.style.backgroundColor = "#e74c3c";
    sup.style.color = "white";
    sup.style.border = "none";

    sup.type = "button";
    mod.type = "button";
    sup.textContent = "Supprimer";
    mod.textContent = "Modifier";

    mod.textContent = "Modifier"
    mod.style.backgroundColor = "#eee";
    mod.style.color = "#333";
    mod.style.border = "1px solid #ccc";

    const titre  = document.createElement("h3");
    const details = document.createElement("div");
    details.className = "task-details";
    titre.textContent = name.value;
    taskBlock.append(titre);
    const line = textarea.value.split("\n");
    /**textarea renvoie un string ex : ligne1\nligne2\nligne3 */
    /** rappel: le split, return une liste en supprimant le caractere en parametre */
    for (var i = 0 ; i < line.length ; i++){
        const p = document.createElement("p");
        p.textContent = line[i];
        details.append(p);
    }
    details.append(mod);
    details.append(sup);
    taskBlock.append(details);
    tasks.append(taskBlock);
    initTaskItem(taskBlock);

}
document.getElementById("ajouter").addEventListener("click",add_tasks);
document.querySelectorAll(".task-item").forEach(function(task){
    initTaskItem(task);
});