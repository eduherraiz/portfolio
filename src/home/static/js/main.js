jQuery(document).ready(function($) {


    /*======= Skillset *=======*/
    
    $('.level-bar-inner').css('width', '0');
    
    $(window).on('load', function() {

        $('.level-bar-inner').each(function() {
        
            var itemWidth = $(this).data('level');
            
            $(this).animate({
                width: itemWidth
            }, 800);
            
        });

    });
    
    /* Bootstrap Tooltip for Skillset */
    $('.level-label').tooltip();

    /* jQuery RSS - https://github.com/sdepold/jquery-rss */
    $("#rss-feeds").rss(
    
        //Change this to your own rss feeds
        blog_url,

        {
        // how many entries do you want?
        // default: 4
        // valid values: any integer
        limit: blog_entries,
        
        // the effect, which is used to let the entries appear
        // default: 'show'
        // valid values: 'show', 'slide', 'slideFast', 'slideSynced', 'slideFastSynced'
        effect: 'slideFastSynced',
        
        // outer template for the html transformation
        // default: "<ul>{entries}</ul>"
        // valid values: any string
        layoutTemplate: "<div class='item'>{entries}</div>",
        
        // inner template for each entry
        // default: '<li><a href="{url}">[{author}@{date}] {title}</a><br/>{shortBodyPlain}</li>'
        // valid values: any string
        entryTemplate: '<h3 class="title"><a href="{url}" target="_blank">{title}</a></h3><div><p>{shortBodyPlain}</p><a class="more-link" href="{url}" target="_blank"><i class="fa fa-external-link"></i>Lee más</a></div>'
        
        }
    );

    var initial = true;
    var listTicker = function(options) {

        var defaults = {
            list: [],
            startIndex:0,
            interval: 3000
        }

        var options = $.extend(defaults, options);

        var listTickerInner = function(index) {

            if (options.list.length == 0) return;

            if (!index || index < 0 || index > options.list.length) index = 0;

            var value= options.list[index];

            if (!initial) {
                options.trickerPanel.fadeOut(function() {
                    $(this).html(value).fadeIn();
                });
            }

            var nextIndex = (index + 1) % options.list.length;

            setTimeout(function() {
                initial = false;
                listTickerInner(nextIndex);
            }, options.interval);

        };

        listTickerInner(options.startIndex);
    }

    $(function() {
        listTicker({
            list: words,
            startIndex:0,
            trickerPanel: $('#titulo'),
            interval: interval_profession
        });
    });

});