
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

                formatted_start = moment(start).format('YYYY-MM-DD, hh:mm');
                formatted_end = moment(end).format('YYYY-MM-DD, hh:mm');
                var create_title = nickname + '(' + teamname + ', ' + phone + ')';

                $("#create_title").val(create_title);
                $("#create_start").val(formatted_start);
                $("#create_end").val(formatted_end);
                $("#create_room").val(resources.id);

                started = start
                ended = end

                $(".antosubmit").on("click", function() {
                    var title = $("#create_title").val();

                    if (title) {
                        calendar.fullCalendar('renderEvent',
                        {
                            title: title,
                            start: started,
                            end: ended,
                        },
                        true // make the event "stick"
                        );
                    }

                $('#create_title').val('');

                calendar.fullCalendar('unselect');
$('#calendar').fullCalendar('rerenderEvents');
                $('.antoclose').click();

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