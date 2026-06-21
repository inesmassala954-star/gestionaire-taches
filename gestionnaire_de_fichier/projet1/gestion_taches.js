
/** active le clic sur le titre pour afficher ou masquer le détail */
const initTaskItem = function (taskItem) {
    const titre = taskItem.querySelector("h3");
    titre.addEventListener("click", function () {
        taskItem.classList.toggle("expanded");
    });
 }
    /** classList manipule les classes CSS
     * toggle() veut dire: si la classe existe,elle est supprimer, 
     * sinon elle est rajouter
     * ici toggle est de la bibliotheque classliste
     *
     * ex
     * <div class="task-item">
    <h3>Titre</h3>
    <div class="task-details">
        <p>Description</p>
    </div>
</div>
};
initTaskItem(div)
titre recupere <h3>titre</h3> quand on clique sur le titre,
la class  du div devient "task-item expanded"**/

const deletetasks = function(){
    const task = this.parentElement.parentElement.remove()
}

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
     
    sup.addEventListener("click", deletetasks);

    sup.type = "button";
    mod.type = "button";
    sup.textContent = "Supprimer";
    mod.textContent = "Modifier";

    mod.textContent = "Modifier"
    mod.style.backgroundColor = "#eee";
    mod.style.color = "#333";
    mod.style.border = "1px solid #ccc";

    mod.addEventListener("click", modify_tasks);

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
    updatetask();

}
document.getElementById("ajouter").addEventListener("click",add_tasks);
document.querySelectorAll(".task-item").forEach(function(task){
    initTaskItem(task);
});


const modify_tasks = function () {

    const taskItem = this.closest(".task-item");
    /** closest prend le parent le plus proche qui possede
     * la classe task-item
     */

    const title = taskItem.querySelector("h3");
    const lines = taskItem.querySelectorAll("p");

    const input = document.getElementsByTagName("input")[0];
    const textarea = document.getElementsByClassName("taskinput")[0];

    // remettre les valeurs dans les champs
    input.value = title.textContent;

    let text = "";
    for (let i = 0; i < lines.length; i++) {
        text += lines[i].textContent + "\n";
    }
    textarea.value = text.trim();
    /** trim enleve les espaces et retour a la ligne inutile a la fin */

    // supprimer la tâche actuelle (option simple)
    taskItem.remove();
};

/** la difference entre getelementbytagname et queryselector; getelementbytagname 
 * recupere tous les elements hors que queryselector recupere le premier element 
 * 
 * si tu ajoute un element p, getelementbytagname("p") se met a jour automatiquement
 * queryselectorall  renvoie une liste figée
 */


const updatetask = function (){
    const total = document.getElementsByTagName("h3").length;
    const span = document.getElementById("total");
    span.textContent = total;
    const details = document.getElementsByClassName("task-details");
    let encours = 0 ;
    let terminé = 0
    for(var i = 0 ; i<details.length ; i++){
        if (details[i].textContent.toLowerCase().includes("terminé")){
            terminé +=1;
        }
        else {
            encours +=1
        }
    }
    const done = document.getElementById("done")
    done.textContent = terminé;
    const cours = document.getElementById("cours")
    cours.textContent = encours;
}
