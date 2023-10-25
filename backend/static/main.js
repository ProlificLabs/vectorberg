function search() {
    let searchTerm = document.getElementById("query").value;

    fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            query: searchTerm
        })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = JSON.stringify(data); // Just as an example
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
}
