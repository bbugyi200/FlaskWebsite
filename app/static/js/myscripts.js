// Resizes 'interview' div in about.html to the size of 'leftImg' at first load and
// after the window is resized.
$(window).ready(updateHeight);
$(window).resize(updateHeight);

function updateHeight()
{
    var leftImg = document.getElementById('leftImg');
    var interview = document.getElementById('interview');
    interview.style.height = leftImg.offsetHeight + 'px';
}
