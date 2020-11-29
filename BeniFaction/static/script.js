var request = new XMLHttpRequest()
const app_discover = document.getElementById('discover-scroll')


request.open('GET', 'https://api.globalgiving.org/api/public/projectservice/countries/PH/projects?api_key=722154ad-56ee-4a68-8d5e-c9da74e49fd1', true)
request.onload = function () {
    var data = JSON.parse(this.response)

    if (request.status >= 200 && request.status < 400){
        data.forEach((project) => {
            // card or container
            const card = document.createElement('div')
            card.className = 'card'
            //Contents
            const title =document.createElement('h1')
            title.className = 'title-project'
            title.textContent = project.title
            const desc_contianer = document.createElement('div')
            desc_contianer.className = 'desc_container'

            const description = document.createElement('p')
            description.className = 'description'
            description.textContent = project.activities
            desc_contianer.appendChild(description)
            const picture = document.createElement('div')
            picture.style.backgroundImage = project.image.imagelink[2].url

            card.appendChild(picture)
            card.appendChild(title)
            card.appendChild(desc_contianer)
            app_discover.appendChild(card)
        })   
    }
};request.send()

window.addEventListener("scroll", function() {
    if (window.scrollY > 500) {
        $('.nav-name').fadeOut();
    }
    else {
        $('.nav-name').fadeIn();
    }
},false);