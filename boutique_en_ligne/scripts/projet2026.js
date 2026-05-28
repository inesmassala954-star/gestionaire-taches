// DA SYLVEIRA , MASSALA ET AGOUDJIL

// ===  variables globales === 

// constantes
const MAX_QTY = 9;
//  tableau des produits à acheter
const cart = []
// total actuel des produits dans le panier
let total = 0;


// === initialisation au chargement de la page ===

/**
* Création du Magasin, mise à jour du total initial
* Mise en place du gestionnaire d'événements sur filter
*/
const init = function () {
	createShop();
	updateTotal();
	loadCart();
	const filter = document.getElementById("filter");
	filter.addEventListener("keyup", filterDisplaidProducts);
}


// ==================== fonctions utiles ======================= 

/**
* Crée et ajoute tous les éléments div.produit à l'élément div#boutique
* selon les objets présents dans la variable 'catalog'
*/
const createShop = function () {
	const shop = document.getElementById("boutique");
	for(let i = 0; i < catalog.length; i++) {
		shop.appendChild(createProduct(catalog[i], i));
	}
}

/**
* Crée un élément div.produit qui posséde un id de la forme "i-produit" où l'indice i 
* est correpond au paramètre index
* @param {Object} product - le produit pour lequel l'élément est créé
* @param {number} index - l'indice (nombre entier) du produit dans le catalogue (utilisé pour l'id)
* @return {Element} une div.produit
*/
const createProduct = function (product, index) {
	// créer la div correpondant au produit
	const divProd = document.createElement("div");
	divProd.className = "produit";
	// fixe la valeur de l'id pour cette div
	divProd.id = index + "-product";
	// crée l'élément h4 dans cette div
	divProd.appendChild(createBlock("h4", product.name));
	
	// Ajoute une figure à la div.produit... 
	// /!\ non fonctionnel tant que le code de createFigureBlock n'a pas été modifié /!\ 
	divProd.appendChild(createFigureBlock(product));

	// crée la div.description et l'ajoute à la div.produit
	divProd.appendChild(createBlock("div", product.description, "description"));
	// crée la div.prix et l'ajoute à la div.produit
	divProd.appendChild(createBlock("div", product.price, "prix"));
	// crée la div.controle et l'ajoute à la div.produit
	divProd.appendChild(createOrderControlBlock(index));
	return divProd;
}


/** Crée un nouvel élément avec son contenu et éventuellement une classe
 * @param {string} tag - le type de l'élément créé (example : "p")
 * @param {string} content - le contenu html de l'élément a créé  (example : "bla bla")
 * @param {string} [cssClass] - (optionnel) la valeur de l'attribut 'classe' de l'élément créé
 * @return {Element} élément créé
 */
const createBlock = function (tag, content, cssClass) {
	const element = document.createElement(tag);
	if (cssClass != undefined) {
		element.className =  cssClass;
	}
	element.innerHTML = content;
	return element;
}

/** Met à jour le montant total du panier en utilisant la variable globale total
 */
const updateTotal = function () {
	const montant = document.getElementById("montant");
	montant.textContent = total;
}

// ======================= fonctions à compléter =======================


/**
* Crée un élément div.controle pour un objet produit
* @param {number} index - indice du produit considéré
* @return {Element}
* TODO : AJOUTER les gestionnaires d'événements
*/
const createOrderControlBlock = function (index) {
	const control = document.createElement("div");
	control.className = "controle";

	// crée l'élément input permettant de saisir la quantité
	const input = document.createElement("input");
	input.id = index + "-qte";
	input.type = "number";
	input.step = "1";
	input.value = "0";
	input.min = "0";
	input.max = MAX_QTY.toString();

	// TODO :  Q5 mettre en place le gestionnaire d'événément pour input permettant de contrôler les valeurs saisies
	input.addEventListener("change", verifQuantity);
    input.addEventListener("keyup", verifQuantity);
	control.appendChild(input);

	// Crée le bouton de commande
	const button = document.createElement("button");
	button.className = 'commander';
	button.id = index + "-order";
	control.appendChild(button);

	return control;
}


/** 
* Crée un élément figure correspondant à un produit
* @param {Object} product -  le produit pour lequel la figure est créée
* @return {Element}

*/
const createFigureBlock = function (product) {
	// TODO : code incorrect : à modifier Q4 
	const figure = document.createElement("figure");
  const img = document.createElement("img");

  img.src = product.image; // ex : "images/nounours1.jpg"
  img.alt = product.name; // ex : "Nounours marron"

  figure.appendChild(img);
  return figure;
}


/** 
* @todo Q8
*/
const orderProduct = function(input) {
    const index = parseInt(input.id.split("-")[0], 10);
    const qty = parseInt(input.value, 10);
    if (qty > 0) {
        addProductToCart(index, qty);
        input.value = "0";
        verifQuantity.call(input);
    }
};


// ======================= fonctions à coder =======================

/**
* @todo Q6- Q7
*/
const verifQuantity = function () {
    let qty = parseInt(this.value, 10);
    if (isNaN(qty) || qty < 0) qty = 0;
    if (qty >= MAX_QTY) qty = 0; 
    this.value = qty;

    const button = this.parentNode.querySelector(".commander");

    if (qty > 0) {
        button.disabled = false;
        button.style.opacity = "1";
        button.onclick = () => orderProduct(this); 
    } else {
        button.disabled = true;
        button.style.opacity = "0.25";
        button.onclick = null;
    }
};

const updateCartAmount = function () {
    total = 0;
    const panier = document.querySelector("#panier .achats");
    cart.length = 0;
    const achats = panier.querySelectorAll(".achat");
    for (let i = 0; i < achats.length; i++) {
        const achat = achats[i];
        const index = parseInt(achat.id.replace("achat-", ""), 10);
        if (!catalog[index]) continue;
        const qtyDiv = achat.querySelector(".quantite");
        const qty = parseInt(qtyDiv.textContent, 10);
        total += catalog[index].price * qty;
        cart.push({ index: index, qty: qty });
    }
    updateTotal();
    saveCart();
};

const addProductToCart = function (index, qty) {
    const productData = catalog[index];
    const panier = document.querySelector("#panier .achats");
    if (!panier || !productData) return;

    let existeproduit = panier.querySelector("#achat-" + index);

    if (existeproduit) {
        const quantitediv = existeproduit.querySelector(".quantite");
        let newQty = parseInt(quantitediv.textContent, 10) + qty;
        if (newQty > MAX_QTY) newQty = MAX_QTY;
        quantitediv.textContent = newQty;
    } else {
        const achat = document.createElement("div");
        achat.id = "achat-" + index;
        achat.className = "achat";

        const figure = createFigureBlock(productData);
        const titre = document.createElement("h4");
        titre.textContent = productData.name;

        const quantiteDiv = document.createElement("div");
        quantiteDiv.className = "quantite";
        quantiteDiv.textContent = qty;

        const prixDiv = document.createElement("div");
        prixDiv.className = "prix";
        prixDiv.textContent = productData.price;

        const controle = document.createElement("div");
        controle.className = "controle";

        const btn = document.createElement("button");
        btn.className = "retirer";
        btn.textContent = "Retirer";
        btn.addEventListener("click", function () {
            achat.remove();
            updateCartAmount();
        });

        controle.appendChild(btn);

        achat.appendChild(figure);
        achat.appendChild(titre);
        achat.appendChild(quantiteDiv);
        achat.appendChild(prixDiv);
        achat.appendChild(controle);

        panier.appendChild(achat);
    }

    const input = document.getElementById(index + "-qte");
    input.value = "0";
    verifQuantity.call(input);

    updateCartAmount();
};

const saveCart = function () {
    localStorage.setItem("cart", JSON.stringify(cart));
};

const filterDisplaidProducts = function(event) {
    const search = event.target.value.toLowerCase();
    const produits = document.querySelectorAll("#boutique .produit");
    for (let i = 0; i < produits.length; i++) {
        const prod = produits[i];
        const name = prod.querySelector("h4").textContent.toLowerCase();
        if (name.includes(search)) {
            prod.style.display = "";
        } else {
            prod.style.display = "none";
        }
    }
};


// ===== CHARGEMENT =====
const loadCart = function () {
    const savedCart = localStorage.getItem("cart");
    if (!savedCart) return;

    cart.length = 0;
    total = 0;

    const panier = document.querySelector("#panier .achats");
    panier.innerHTML = "";

    const savedArray = JSON.parse(savedCart);

    for (let i = 0; i < savedArray.length; i++) {
        const item = savedArray[i];
        addProductToCart(item.index, item.qty);
    }
};
// ====================  Exécuter l'initialisation ======================= 
/*Q1*/
document.addEventListener("DOMContentLoaded", function() {
    init();
});