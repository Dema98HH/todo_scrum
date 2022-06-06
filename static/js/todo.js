$(document).ready(function(){

    $("#createButton").click(function(){
            var serializedData = $("#createTaskForm").serialize();

            $.ajax({
                url: $("createTaskForm").data('url'),
                data: serializedData,
                type: 'post',
                success: function(response){
                    $("#taskList").append('<li class="list-group-item list-group-item-light mt-2">'
                    + response.task.name + '<button type="button" class="close float-right mr-2"><span aria-hidden="true">&times;</span></button></li>')
                }
            })

            $('#createTaskForm')[0].reset();
        });

    });