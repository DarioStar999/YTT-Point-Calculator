// MADE BY CHATGPT NON SO JAVASCRIPT

const rows = document.querySelectorAll('tr.border-b');

const data = Array.from(rows)
    .map(row => {
        const cells = row.querySelectorAll('td');
        if (cells.length < 10) return null;

        return {
            username: cells[0]?.querySelector('span')?.innerText.trim() || '',
            team: cells[1]?.innerText.trim() || '',
            kill: cells[3]?.innerText.trim() || '',
            lettiRotti: cells[7]?.innerText.trim() || '',
            finalKill: cells[4]?.innerText.trim() || '',
            morti: cells[5]?.innerText.trim() || ''
        };
    })
    .filter(Boolean);

console.table(data);

console.log(JSON.stringify(data, null, 2));