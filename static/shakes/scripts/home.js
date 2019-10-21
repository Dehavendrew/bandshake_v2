$(document).ready(function(){
    $("article").click(function(){
        if(this.id){
            window.location.href = "http://127.0.0.1:8000/shake/" + this.id
        }
    })
})

function getDocs(resumePath){
    var doc = document.createElement("IFRAME")
    doc.id = 'doc'
    doc.src = resumePath
    doc.style.height = "250px"
    doc.style.width = "200px"
    doc.scrolling = "no"
    doc.style.margin = "5px"
    doc.style.border = "thick solid seagreen"
    document.getElementById('doc_box').appendChild(doc)
}


function createEventPage(){
    window.location.href = "http://127.0.0.1:8000/events/create/"
}

function joinEventPage(){
    window.location.href = "http://127.0.0.1:8000/connect/"
}

private_clicked = false
function showPersonalForm(){
    if(!private_clicked){
        $("#private_content").load("/profile/private/")
        private_clicked = true
    }
    else{
        $("#private_content").remove()
        var temp = document.createElement("DIV")
        temp.id = "private_content"
        document.getElementById("private_space").appendChild(temp)
        private_clicked = false
    }
}

resume_clicked = false
function showResumeForm(){
    if(!resume_clicked){
        $("#resume_content").load("/profile/get-resume/")
        resume_clicked = true
    }
    else{
        $("#resume_content").remove()
        var temp = document.createElement("DIV")
        temp.id = "resume_content"
        document.getElementById("resume_space").appendChild(temp)
        resume_clicked = false
    }
}

flyer_clicked = false
function showFlyerForm(){
    if(!flyer_clicked){
        $("#flyer_content").load("/profile/get-flyer/")
        flyer_clicked = true
    }
    else{
        $("#flyer_content").remove()
        var temp = document.createElement("DIV")
        temp.id = "flyer_content"
        document.getElementById("flyer_space").appendChild(temp)
        flyer_clicked = false
    }
}

public_clicked = false
function showPublicForm(){
    if(!public_clicked){
        $("#public_content").load("/profile/get-public/")
        public_clicked = true
    }
    else{
        $("#public_content").remove()
        var temp = document.createElement("DIV")
        temp.id = "public_content"
        document.getElementById("public_space").appendChild(temp)
        public_clicked = false
    }
}

company_Create_clicked = false
function showNewCompanyForm(){
    if(!company_Create_clicked){
        $("#register_company_content").load("http://127.0.0.1:8000/company/register/")
        company_Create_clicked = true
    }
    else{
        $("#register_company_content").remove()
        var temp = document.createElement("DIV")
        temp.id = "register_company_content"
        document.getElementById("register_company_space").appendChild(temp)
        company_Create_clicked = false
    }
}