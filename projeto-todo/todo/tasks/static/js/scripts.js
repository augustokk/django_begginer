$(document).ready(function() {

    // DELETE BUTTON
    // create a variable that will select that delete element 
    var deleteBtn = $('.delete-btn');

    // SEARCH BUTTON
    // create a variable to the search button (using id --> #)
    var searchBtn = $('#search-btn');
    // create a variable to the search form
    var searchForm = $('#search-form');

    // DELETE FUNCTION
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

    // SEARCH FUNCTION
    // function that activates when click on the seacrh icon
    $(searchBtn).on('click', function() {
        // that activates the searchForm submit
        searchForm.submit();
    });
});


