function scan() {
    const ips = document.getElementById("ips").value.split("\n");

    fetch("/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ips: ips })
    })
    .then(response => response.json())
    .then(data => {
        const table = document.getElementById("results");
        table.innerHTML = "";

        data.forEach(item => {
            table.innerHTML += `
                <tr>
                    <td>${item.ip}</td>
                    <td>${item.country}</td>
                    <td>${item.isp}</td>
                    <td>${item.abuse_score}</td>
                    <td>${item.reports}</td>
                    <td>${item.vt_malicious}</td>
                    <td>${item.vt_suspicious}</td>
                </tr>
            `;
        });
    });
}