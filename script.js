const fileList = [
    { name: "Car.csv", type: "csv", size: "3.8 KB" },
    { name: "Housing.csv", type: "csv", size: "29.9 KB" },
    { name: "Salary_Data.csv", type: "csv", size: "348 KB" },
    { name: "california_housing.csv", type: "csv", size: "1.2 MB" },
    { name: "customer_satisfaction.csv", type: "csv", size: "1 KB" },
    { name: "prog1.py", type: "py", size: "893 B" },
    { name: "prog2.py", type: "py", size: "958 B" },
    { name: "prog3.py", type: "py", size: "392 B" },
    { name: "prog4.py", type: "py", size: "1.4 KB" },
    { name: "prog5.py", type: "py", size: "676 B" },
    { name: "prog6.py", type: "py", size: "724 B" },
    { name: "prog7.py", type: "py", size: "913 B" },
    { name: "Prog8.py", type: "py", size: "1.3 KB" },
    { name: "prog9.py", type: "py", size: "965 B" },
    { name: "prog10.py", type: "py", size: "784 B" },
    { name: "prog11.py", type: "py", size: "824 B" },
    { name: "requirements.txt", type: "txt", size: "56 B" }
];

const grid = document.getElementById('fileGrid');
const searchInput = document.getElementById('searchInput');
const filterBtns = document.querySelectorAll('.filter-btn');

function getIcon(type) {
    switch(type) {
        case 'py': return '🐍';
        case 'csv': return '📊';
        case 'txt': return '📄';
        default: return '📁';
    }
}

function renderFiles(files) {
    grid.innerHTML = '';
    files.forEach((file, index) => {
        const card = document.createElement('div');
        card.className = 'file-card';
        card.style.animationDelay = `${index * 50}ms`;
        
        card.innerHTML = `
            <div class="card-header">
                <div class="file-icon">${getIcon(file.type)}</div>
                <div class="file-info">
                    <h3>${file.name}</h3>
                    <div class="file-meta">
                        <span class="badge badge-${file.type}">${file.type.toUpperCase()}</span>
                        <span>${file.size}</span>
                    </div>
                </div>
            </div>
            <a href="./${file.name}" download class="download-btn">
                <span>Download File</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
            </a>
        `;
        grid.appendChild(card);
    });
}

function filterFiles() {
    const searchTerm = searchInput.value.toLowerCase();
    const activeFilter = document.querySelector('.filter-btn.active').dataset.filter;
    
    const filtered = fileList.filter(file => {
        const matchesSearch = file.name.toLowerCase().includes(searchTerm);
        const matchesType = activeFilter === 'all' || file.type === activeFilter;
        return matchesSearch && matchesType;
    });
    
    renderFiles(filtered);
}

// Event Listeners
searchInput.addEventListener('input', filterFiles);

filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        filterBtns.forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        filterFiles();
    });
});

// Initial Render
renderFiles(fileList);
