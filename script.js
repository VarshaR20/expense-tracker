let total = 0;

function addExpense() {
    let category = document.getElementById("category").value;
    let amount = document.getElementById("amount").value;

    if (category === "" || amount === "") {
        alert("Please enter all fields");
        return;
    }

    let li = document.createElement("li");
    li.innerText = category + " - ₹" + amount;
    document.getElementById("expenseList").appendChild(li);

    total += parseInt(amount);
    document.getElementById("total").innerText = total;

    document.getElementById("category").value = "";
    document.getElementById("amount").value = "";
}
