
var insert = function(array, rightIndex, value) {
    
    while (value < array[rightIndex]) {
        var temp = array[rightIndex];
        array[rightIndex+1] = temp;
        rightIndex--;
    }
    array[rightIndex+1] = value;
    
};

var array = [3, 5, 7, 11, 13, 2, 9, 6];

insert(array, 4, 2);
console.log("Array after inserting 2:  " + array);
//Program.assertEqual(array, [2, 3, 5, 7, 11, 13, 9, 6]);

insert(array, 5, 9);
console.log("Array after inserting 9:  " + array);
//Program.assertEqual(array, [2, 3, 5, 7, 9, 11, 13, 6]);

insert(array, 6, 6);
console.log("Array after inserting 6:  " + array);
//Program.assertEqual(array, [2, 3, 5, 6, 7, 9, 11, 13]);
