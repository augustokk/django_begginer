$(document).ready(function() {
    // create a variable that will select that delete element 
    var deleteBtn = $('.delete-btn');

    // function that activates when click with an parameter (e)vent
    $(deleteBtn).on('click', function(e) {
        
        // that will prevent that delete button to delete straigth away
        e.preventDefault();

        // create a link when we want to delete the task
        var delLink =$(this).attr('href');

        // create message to check if wants delete
        var result = confirm('Do you want to delete this task?')

        // if user confirms that wants to delete
        if(result){
            window.location.href = delLink
        }

    });
});