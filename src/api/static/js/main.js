document.getElementById("priceForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    const response = await fetch("/predict-price", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("result").innerHTML =
        `<h3>Recommended Price: ${data.recommended_price}</h3>
         <p>Predicted Demand: ${data.predicted_demand}</p>`;
});
