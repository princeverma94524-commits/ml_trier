const ctx = document.getElementById('priceChart');

new Chart(ctx, {
    type: 'line',
    data: {
        labels: [400, 450, 500, 550, 600],
        datasets: [{
            label: 'Demand',
            data: [160, 140, 125, 105, 90],
            borderWidth: 2
        }]
    }
});
