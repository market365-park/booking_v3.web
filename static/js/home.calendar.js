function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};
var csrftoken = getCookie('csrftoken');

/* CALENDAR */

function  init_calendar() {
    if( typeof ($.fn.fullCalendar) === 'undefined'){ return; }
    console.log('init_calendar');

    var date = new Date(),
        d = date.getDate(),
        m = date.getMonth(),
        y = date.getFullYear(),
        started,
        categoryClass;

    var calendar = $('#calendar').fullCalendar({
        schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',

        header: {
            center: 'title',
            left: 'agendaDay,agendaWeek,month',
            right: 'prev,next today'
        },
        height: 604,
        events: room_bookings,
        resources: rooms,

        firstDay: 0, //  1(Monday) this can be changed to 0(Sunday) for the USA system
        defaultView: 'agendaDay',
        views: {
            agendaDay:{
                titleFormat: 'ddd, MMMM D',
                groupByResource: true,
            },
            agendaWeek: {
                titleFormat: 'D, MMMM',
            },
            month: {
                titleFormat: 'MMMM, YYYY',
            }
        },
        timezone: 'Asia/Seoul',
        nowIndicator: true,
        allDaySlot: false,
        minTime: "07:00:00",
        maxTime: "20:00:00",
        businessHours: {
        // days of week. an array of zero-based day of week integers (0=Sunday)
            dow: [1, 2, 3, 4, 5], // Monday - Thursday
            start: '08:00', // a start time (10am in this example)
            end: '19:00' // an end time (6pm in this example)
        },

        navLinks: true,
//            navLinkDayClick: function (date) {
//                $('#calendar').fullCalendar('gotoDate', date);
//                $('#calendar').fullCalendar('changeView', 'agendaDay');
//            },

        selectOverlap: false,
        selectable: true,
        selectHelper: true,
        select: function(start, end, jsEvent, view, resources) {
            $('#fc_create').click();

            var formatted_start = moment(start).format('YYYY-MM-DD HH:mm');
            var formatted_end = moment(end).format('YYYY-MM-DD HH:mm');
            var event_title = nickname + '(' + teamname + ', ' + phone + ')';
            var event_start = start;
            var event_end = end;
            var event_resources = resources;

            $("#create_title").val(event_title);
            $("#create_start").val(formatted_start);
            $("#create_end").val(formatted_end);
            $("#create_room").val(resources.id);

            if (event_title) {
                eventData = {
                    title: event_title,
                    start: event_start,
                    end: event_end,
                    resourceId : event_resources.id,
                };
                $('#calendar').fullCalendar('renderEvent', eventData, true);
                true // make the event "stick"
            };
            $('#calendar').fullCalendar('unselect');

            $(".antosubmit").on("click", function() {
                function csrfSafeMethod(method) {
                    // these HTTP methods do not require CSRF protection
                    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
                };

                $.ajaxSetup({
                    beforeSend: function(xhr, settings) {
                        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }
                    }
                });

                var event_data
                event_data = new FormData();

                event_data.append("title", event_title);
                event_data.append('start_time', formatted_start);
                event_data.append('end_time', formatted_end);
                event_data.append('room_id', event_resources.id);

                $.ajax({
                    type: "POST",
                    url: "/room/create/",
                    data: event_data,
                    enctype: 'multipart/form-data',
                    processData: false,
                    contentType: false,
//                    cache: false,
                    success: function (data) {
                        console.log(data);
                    },
                });

                event_data = false;
                formatted_start = false;
                formatted_end = false;
                event_title = false;
                event_start = false;
                event_end = false;
                event_resources = false;

                $('.antoclose').click();

                return false;

            });
        },

        editable: false,
        eventLimit: true, // allow "more" link when too many events
        eventClick: function(calEvent, jsEvent, view) {
            $('#fc_edit').click();
            $('#title2').val(calEvent.title);

            categoryClass = $("#event_type").val();

            $(".antosubmit2").on("click", function() {
                calEvent.title = $("#title2").val();

                calendar.fullCalendar('updateEvent', calEvent);
                $('.antoclose2').click();
            });

            calendar.fullCalendar('unselect');
        },

    });

};

$(document).ready(function() {
    init_calendar();
});