$(window).load(init());

function init() {
    $('#num').slider({
        formatter: function(value) {
            return 'Current value: ' + value;
        }
    });
}
