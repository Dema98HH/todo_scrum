$(document).ready(function(){

var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    $("#createButton").click(function(){
            var serializedData = $("#createTaskForm").serialize();

            $.ajax({
                url: $("createTaskForm").data('url'),
                data: serializedData,
                type: 'post',
                success: function(response){
                    $("#taskList").append('<div class="list-group-item list-group-item-light mt-2" data-id="' + response.task.id + '" id="taskCard">'
                    + response.task.name + '<button type="button" class="close float-right mr-2"><span aria-hidden="true">&times;</span></button></div>')
                }
            })

            $('#createTaskForm')[0].reset();

        });

        $("#taskList").on('click', '.list-group-item', function(){
            var dataId = $(this).data('id' );
            $.ajax({
                url: '/tasks/' + dataId + '/completed/',
                data: {
                    csrfmiddlewaretoken: csrfToken,
                    id: dataId
                },
                type: 'post',
                success: function(){
                    var cardItem = $('#taskCard[data-id="' + dataId + '"]');
                    cardItem.css('text-decoration', 'line-through').hide().slideDown();
                    $("#taskList").append(cardItem);
                }
            });
        });

    });