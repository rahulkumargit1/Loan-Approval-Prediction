document.getElementById('loanForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = {
        no_of_dependents: parseInt(document.getElementById('no_of_dependents').value),
        education: document.getElementById('education').value,
        self_employed: document.getElementById('self_employed').value,
        income_annum: parseFloat(document.getElementById('income_annum').value),
        loan_amount: parseFloat(document.getElementById('loan_amount').value),
        loan_term: parseInt(document.getElementById('loan_term').value),
        cibil_score: parseInt(document.getElementById('cibil_score').value),
        residential_assets_value: parseFloat(document.getElementById('residential_assets_value').value),
        commercial_assets_value: parseFloat(document.getElementById('commercial_assets_value').value),
        luxury_assets_value: parseFloat(document.getElementById('luxury_assets_value').value),
        bank_asset_value: parseFloat(document.getElementById('bank_asset_value').value)
    };

    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (result.status === 'success') {
            document.getElementById('result').innerHTML = 
                `Prediction: ${result.prediction} (Probability of Approval: ${(result.probability * 100).toFixed(2)}%)`;
        } else {
            document.getElementById('result').innerHTML = `Error: ${result.message}`;
        }
    } catch (error) {
        document.getElementById('result').innerHTML = `Error: ${error.message}`;
    }
});