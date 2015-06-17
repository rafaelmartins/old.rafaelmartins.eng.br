$(function() {
    var $container = $('article'),
        $elements = $('article img, article iframe');
    $elements.each(function() {
        $(this).data('ratio', this.width / this.height)
               .data('orig_width', this.width)
               .removeAttr('height')
               .removeAttr('width');
    });
    $(window).resize(function() {
        var $container_width = $container.width();
        $elements.each(function() {
            var $element = $(this);
            if ($element.is('iframe') || $element.data('orig_width') >= $container_width)
                $element.width($container_width)
                        .height($container_width / $element.data('ratio'));
        });
    }).resize();
});

