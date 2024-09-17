class FilterPanel {
    constructor(savedFilters) {
        this.data // all posible filters

        this.filters = savedFilters ? JSON.parse(savedFilters) : {}

        this.checkboxFilters = ["created_at", "last_modified", "downloads", "likes", "size_categories"]
    }

    async set() {
        
        await this.fetchData()

        await this.generateFilters()

        await this.restoreFilters()

        await this.setNetworkOptions()

    }

    getSelectedFilters() {
        return this.filters
    }

    // Function to capitalize the first letter and remove underscores or hyphens from a string
    prettyTitle(key) {
        // Replace underscores or hyphens with spaces, capitalize first letter, and then capitalize the rest
        return key
            .replace(/[_-]/g, ' ') // Replace underscores or hyphens with spaces
            .replace(/\b\w/g, char => char.toUpperCase()); // Capitalize the first letter of each word
    }

    saveFilters(key, value) {   
       
        if (this.filters[key]) {
            if (Array.isArray(value)) {
                if (!this.filters[key].length) {
                    this.filters[key] = value
                } else if (this.filters[key].every(d => value.includes(d)))
                    this.filters[key] = []
                else this.filters[key] = value
            }
            else if (this.filters[key].includes(value)) {
                this.filters[key] = this.filters[key].filter(d => d !== value)
            } else {
                this.filters[key].push(value)
            }
        } else {
            if (Array.isArray(value))
                this.filters[key] = value
            else this.filters[key] = [ value ]
        }

        console.log(this.filters)

        window.sessionStorage.setItem('filters', JSON.stringify(this.filters))
    }

    async restoreFilters() {
        // let savedFilters = window.sessionStorage.getItem('filters')
        
        console.log("savedFilters", this.filters)

        // update the selections according to filters in the sessionStorage
        for (let key of Object.keys(this.filters)) {
            const values = this.filters[key]

            if (this.checkboxFilters.includes(key)) {
                for (let value of values) {
                    const checkbox = document.querySelector(`input[name="${key}"][value="${value}"]`);
                    if (checkbox) {
                        checkbox.checked = true; // Check the saved checkboxes
                    }
                }
            } else {
                for (let value of values) {
                    this.renderSelectedValue(key, value)
                }
            }
        }
    }
    

    // Function to create input with datalist for strings, allowing multiple selection
    createDataListInput(key, values) {
        const options = values.map(item => `<option value="${item.value}">${item.name} (${item.count})</option>`).join('');
        const prettyKey = this.prettyTitle(key);

        return `
            <div class="mb-3">
                <label for="${key}" class="form-label">${prettyKey}</label>
                <input type="text" class="form-control multi-select-input" id="${key}-input" placeholder="Choose ${prettyKey}..." list="${key}-datalist">
                <datalist id="${key}-datalist">
                    ${options}
                </datalist>
                <div id="${key}-selected" class="selected-items mt-2"></div>
            </div>
        `;
    }

   // Function to initialize multi-select functionality for all inputs at once
    initAllMultiSelectInputs() {
        const multiSelectInputs = document.querySelectorAll('.multi-select-input');
        
        multiSelectInputs.forEach(inputElement => {
            const key = inputElement.id.replace('-input', '');  // Extract the key from the input ID
            this.initMultiSelectInput(key);  // Initialize multi-select for each input
        });
    }

    // Function to render the selected values
    renderSelectedValue(key, value) {
        const _this = this;

        const selectedContainer = document.querySelector(`#${key}-selected`);

        const span = document.createElement('span');
        span.setAttribute('class', "badge bg-light text-dark mr-2");
        span.style.marginLeft = '10px'
        span.textContent = value

        const button = document.createElement('button');
        button.setAttribute('class', "btn btn-sm btn-danger remove-btn");
        button.setAttribute('type', 'button');
        button.style.marginLeft = '5px'
        button.innerHTML = '&times;';  

        button.addEventListener('click', function() {
            _this.saveFilters(key, value);  // Save filters with the current key and value
            this.parentNode.remove();  // Remove the badge
        });

        span.appendChild(button);
        selectedContainer.appendChild(span);

    }

    // Function to initialize multi-select functionality for a single input
    initMultiSelectInput(key) {
        const inputElement = document.querySelector(`#${key}-input`);


        // Add event listener to input field to capture selection
        inputElement.addEventListener('input', (event) => {
            
            const value = event.target.value.trim();
            let validValues = Object.keys(this.data[key])
        
            if (value && validValues.includes(value)) {
                if (this.filters[key] && this.filters[key].includes(value)) return

                this.renderSelectedValue(key, value);  // Render the updated list
                this.saveFilters(key, value)

                inputElement.value = '';  // Clear the input after adding the selection
            }
            
        });

        // Handle Enter key or value selection from the datalist
        inputElement.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' && inputElement.value.trim()) {
                const value = inputElement.value.trim();
                
                if (this.filters[key] && this.filters[key].includes(value)) return
                
                this.renderSelectedValue(key, value);  // Render the updated list
                this.saveFilters(key, value)

                inputElement.value = '';  // Clear the input after selection
            }
        });
    }


    // Function to convert range string to comparable numeric values
    convertToNumber(str) {
        const value = str.match(/\d+\.?\d*/g);  // Extract the number part
        const unit = str.match(/[KMGTB]/);      // Extract the unit (K, M, B, T)
        
        let num = parseFloat(value[0]);         // Get the first number in the range
        
        if (unit) {
            switch (unit[0]) {
                case 'K': return num * 1e3;     // Thousand
                case 'M': return num * 1e6;     // Million
                case 'B': return num * 1e9;     // Billion
                case 'T': return num * 1e12;    // Trillion
            }
        }
        
        return num;  // Return plain number if no unit found (e.g., "n<1K")
    }

    // Function to create a radio list for 'size_categories'
    createCheckboxList(key, values) {
        const prettyKey = this.prettyTitle(key);
        
        const checkboxButtons = values.map(item =>
            `
                <div class="form-check">
                    <input class="form-check-input filter-checkboxes" type="checkbox" name="${key}" id="${key}-${item.value}" value="${item.value}">
                    <label class="form-check-label " for="${key}-${item.value}">
                        ${item.name} <span style='margin-left: 5px; font-size: 10px;'>(${item.count})</span>
                    </label>
                </div>
            `
        ).join('');

        return `
            <div class="mb-3">
                <label class="form-label">${prettyKey}</label>
                ${checkboxButtons}
            </div>
        `;
    }

    setInteractors() {
        
        const _this = this;

        this.initAllMultiSelectInputs()

        let checkboxes = document.querySelectorAll('.filter-checkboxes')
        for (let cb of checkboxes) {
            cb.addEventListener('change', function () {
                let value = this.value
                if (['downloads', 'likes'].includes(this.name)) {
                    value = value.split('-').map(d => +d)                    
                }
                console.log(this.name, this.value, value)
                _this.saveFilters(this.name, value)        
            })
        }

    }


    // Function to generate filters dynamically based on data
    async generateFilters() {
        const filtersContainer = document.querySelector('#filters-container');

        function getLanguageName(code) {
            try {
                const languageName = new Intl.DisplayNames(['en'], { type: 'language' });
                return `${languageName.of(code)} (${code})` || `Unknown (${code})`;
            } catch (error) {
                console.log('Error fetching language name:', error);
                return `Unknown (${code})`;
            }
        }

        for (let key of Object.keys(this.data)) {
            const values = this.data[key];

            // Special case for 'size_categories' - create checkbox list
            if (this.checkboxFilters.includes(key) ) {
                let uniqueValues = Object.keys(values).map(value => ({
                    value: value,
                    name: value.replace(/</g, ' &lt; ').replace(/>/g, ' &gt; ').trim(),
                    count: values[value]
                }));

                uniqueValues.sort((a, b) => this.convertToNumber(a.name) - this.convertToNumber(b.name));
                // const sortedValues = uniqueValues.map(item => `${item.name}&nbsp;&nbsp;&nbsp;&nbsp;(${item.count} datasets)`);

                filtersContainer.innerHTML += this.createCheckboxList(key, uniqueValues);
            } 
            else if (key === 'language') {
                let uniqueValues = Object.keys(values).map(value => ({
                    value: value,
                    name: getLanguageName(value),
                    count: values[value]
                }));

                uniqueValues.sort((a, b) => b.count - a.count);
                // const sortedValues = uniqueValues.map(item => `${item.name} (${item.count} datasets)`);
                filtersContainer.innerHTML += this.createDataListInput(key, uniqueValues);
            } 
            // Create datalist input for string values
            else {
                let uniqueValues = Object.keys(values).map(key => ({
                    value: key,
                    name: key,
                    count: values[key]
                }));

                uniqueValues.sort((a, b) => b.count - a.count);
                // const sortedValues = uniqueValues.map(item => `${item.name} (${item.count} datasets)`);
                filtersContainer.innerHTML += this.createDataListInput(key, uniqueValues);
            }
        }

        this.setInteractors()
    }

    async setNetworkOptions() {
        let variables = ['dataset', 'task_categories', 'task_id', 'modality', 'license', 'format', 'language']

        this.setSelect(variables, '#source-select', 'task_categories')
        this.setSelect(variables, '#target-select', 'task_categories')
        this.setSelect(variables, '#link-select', 'dataset')

        let themeVariables = ['modality', 'license', 'format', 'size_categories', 'language']
        this.setSelect(themeVariables, '#theme-select', 'license')
    } 

    async setSelect(data, selector, selectedValue) {
        d3.select(selector)
            .selectAll('option')
            .data(data)
            .join(
                enter => enter.append('option'),
                update => update,
                exit => exit.remove()
            )
            .attr('value', d => d)
            .text(d => this.prettyTitle(d))
            .property('selected', d => d === selectedValue)
    }


    async fetchData() {
        try {
            const response = await fetch('/mgnlp/data/filters', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            console.log(response)
    
            if (!response.ok) {
                console.error('There was a problem.');
                return;
            }
    
            this.data = await response.json()
            console.log('filters = ', this.data)
    
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
}