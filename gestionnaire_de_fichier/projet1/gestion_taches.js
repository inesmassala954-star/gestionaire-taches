
/** une fonction qui ajoute les taches  */
const add_tasks = function(){
    const name = document.getElementsByTagName("input")[0];
    const tasks = document.getElementsByClassName("tache")[0];
    const textarea = document.getElementsByClassName("taskinput")[0];
    const taskBlock = document.createElement("div");
    const sup = document.createElement("button");
    const mod = document.createElement("button");
    sup.textContent = "Supprimer"
    sup.style.backgroundColor = "#e74c3c";
    sup.style.color = "white";
    sup.style.border = "none";

    mod.textContent = "Modifier"
    mod.style.backgroundColor = "#eee";
    mod.style.color = "#333";
    mod.style.border = "1px solid #ccc";

    const titre  = document.createElement("h3");
    taskBlock.append(titre);
    titre.textContent = name.value;
    const line = textarea.value.split("\n");
    /**textarea renvoie un string ex : ligne1\nligne2\nligne3 */
    /** rappel: le split, return une liste en supprimant le caractere en parametre */
    for (var i=0;i<line.length;i++){
        const p = document.createElement("p");
        p.textContent=line[i];
        taskBlock.append(p);
    }
    taskBlock.append(mod); 
    taskBlock.append(sup);
    tasks.append(taskBlock)

}
document.getElementById("ajouter").addEventListener("click",add_tasks)