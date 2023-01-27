let StudentsAffairs = document.getElementById("SA");
StudentsAffairs.onclick = function() {
    window.location.href = "{% url 'StudentAffairs' %}";
};