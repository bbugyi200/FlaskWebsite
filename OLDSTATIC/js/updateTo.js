var LF = document.getElementById("topLeftFrame");
var LR = document.getElementById("topRightFrame");

function RepopulateElements()
{
    if (document.getElementById("iframe1") != null)
    {   
        var el = document.getElementById("iframe1");
        el.parentNode.removeChild(el);
    }
    if (document.getElementById("topLeftFrame") === null) 
    {
        document.getElementById("innerBody").appendChild(LF);
    }
    if (document.getElementById("topRightFrame") === null)
    {
        document.getElementById("innerBody").appendChild(LR);
    }
}

function updateToAbout()
{   
    RepopulateElements();
    var x = document.getElementById("topLeftFrame");
    x.innerHTML = "<h2>About Me</h2> \
                   <p> \
                   All about little ole me... \
                   All about little ole me... \
                   All about little ole me... \
                   All about little ole me... \
                   All about little ole me... \
                   All about little ole me... \
                   All about little ole me... \
                   All about little ole me... \
                   </p>";
}

function updateToHome()
{
    RepopulateElements();
    var x = document.getElementById("topLeftFrame");
    x.innerHTML = "<h2>What's this site all about?</h2> \
                   <p> \
            This is a quick description of what this website is about...\
            I will write alll about this website right here..\
            And blah blah blah... \
            This is a quick description of what this website is about...\
            I will write alll about this website right here..\
            And blah blah blah... \
            This is a quick description of what this website is about...\
            I will write alll about this website right here..\
            And blah blah blah... \
            This is a quick description of what this website is about...\
            I will write alll about this website right here..\
            And blah blah blah... \
            This is a quick description of what this website is about...\
            I will write alll about this website right here..\
            And blah blah blah... \
            This is a quick description of what this website is about...\
            I will write alll about this website right here..\
            And blah blah blah... \
                   </p>";
}

function updateToCoursework()
{
    RepopulateElements();
    var x = document.getElementById("topLeftFrame");
    x.innerHTML = "<h2>College Coursework</h2> \
        <p> \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        I should recreate my past and predicted course spreadsheet here. \
        </p>";
}

function updateToResume()
{
    var x = document.getElementById("topLeftFrame");
    LF = x;
    x.parentNode.removeChild(x);

    var y = document.getElementById("topRightFrame");
    LR = y;
    y.parentNode.removeChild(y);

    ifrm = document.createElement("IFRAME");
    ifrm.setAttribute("src", "../static/resume/dummy_resume.pdf");
    ifrm.setAttribute("id", "iframe1");
    document.getElementById("innerBody").appendChild(ifrm);
}
