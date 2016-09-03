var str = $('input').value

// Match all numbers not 0 and 1
var numbers = str.match(/[^\D01]/g);

var compositeSum = 0;
var primeSum = 0;

for (i = 0; i < numbers.length; i++) {
    var temp_number = parseInt( numbers[ i ] );

    if( temp_number == 2 || temp_number == 3 || temp_number == 5 || temp_number == 7 ) {
        primeSum += temp_number;
    }
    else {
        compositeSum += temp_number;
    }
}

var composite_prime_product = compositeSum * primeSum;

// Match all non-numbers
var non_numbers = str.match(/[\D]/g);

var incremented_string = '';

for (i = 0; i < 25; i++ ) {
    incremented_string += String.fromCharCode( non_numbers[ i ].charCodeAt( 0 ) + 1 );
}

incremented_string += composite_prime_product;

$('form input').value = incremented_string;
