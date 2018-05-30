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


function getQuerystring(paramName) {
var _tempUrl = window.location.search.substring(1); //url에서 처음부터 '?'까지 삭제
var _tempArray = _tempUrl.split('&'); // '&'을 기준으로 분리하기

for (var i = 0; _tempArray.length; i++) {
    var _keyValuePair = _tempArray[i].split('='); // '=' 을 기준으로 분리하기

    if (_keyValuePair[0] == paramName) { // _keyValuePair[0] : 파라미터 명
        // _keyValuePair[1] : 파라미터 값
        return _keyValuePair[1];
    } else {
        return null;
    }
}
}

var init_day = getQuerystring('start');
if (init_day == null) {
    init_day = new Date();
}


/* CALENDAR */

function  init_calendar() {
    if( typeof ($.fn.fullCalendar) === 'undefined'){ return; }
    console.log('init_calendar');

    var calendar = $('#calendar').fullCalendar({
        schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
        now: init_day,
        themeSystem: 'bootstrap3',
        bootstrapGlyphicons: {
          close: 'glyphicon-remove',
          prev: 'glyphicon-chevron-left',
          next: 'glyphicon-chevron-right',
          prevYear: 'glyphicon-backward',
          nextYear: 'glyphicon-forward'
        },
        header: {
            center: 'title',
            left: 'agendaDay,agendaWeek,month',
            right: 'prev,next myCustomButton'
        },
        customButtons: {
            myCustomButton: {
                text: 'Today',
                click: function () {
                    location.href = '/';
                }
            }
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
            start: '10:00', // a start time (10am in this example)
            end: '16:00' // an end time (6pm in this example)
        },

//        navLinks: true,
        navLinkDayClick: function (date) {
            $('#calendar').fullCalendar('gotoDate', date);
            $('#calendar').fullCalendar('changeView', 'agendaDay');
        },

        selectOverlap: false,
        selectable: true,
        selectHelper: true,
        select: function(start, end, jsEvent, view, resources) {
            if (view.name == 'month' | view.name == 'agendaWeek') {
                $('#calendar').fullCalendar('gotoDate', start);
                $('#calendar').fullCalendar('changeView', 'agendaDay');
                $('.antoclose').click();
                return false;
            };

            $('#fc_create').click();

            var event_title = nickname + '(' + teamname + ', ' + phone + ')';
            var formatted_start = moment(start).format('YYYY-MM-DD HH:mm');
            var formatted_end = moment(end).format('YYYY-MM-DD HH:mm');

            $("#title").val(event_title);
            $("#start_time").val(formatted_start);
            $("#end_time").val(formatted_end);
            $("#room_id").val(resources.id);

            $(".create_antosubmit").on("click", function() {
                if (event_title) {
                    calendar.fullCalendar('renderEvent',
                        {
                        title: event_title,
                        start: start,
                        end: end,
                        resourceId : resources.id
                        },
                        true // make the event "stick"
                    );
				}
//                $('.create_antoclose').click();
//                return false;
            });
        },
        editable: false,
        eventLimit: true, // allow "more" link when too many events
        eventClick: function(calEvent, jsEvent, view) {
            $('#fc_edit').click();
            var formatted_start = moment(calEvent.start).format('YYYY-MM-DD HH:mm');
            var formatted_end = moment(calEvent.end).format('YYYY-MM-DD HH:mm');
            $("#delete_title").val(calEvent.title);
            $("#delete_start_time").val(formatted_start);
            $("#delete_end_time").val(formatted_end);
            $("#delete_room_id").val(calEvent.resourceId);
            $("#delete_event_id").val(calEvent.id);



            $(".delete_antosubmit").on("click", function() {
                $('.delete_antoclose').click();
            });
            calendar.fullCalendar('unselect');
        },
    });
};

$(document).ready(function() {
    init_calendar();
});