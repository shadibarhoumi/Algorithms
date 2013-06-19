function merge(a, b) {
	if (a.length === 0) { return b; }
	if (b.length === 0) { return a; }
	if (a[0] <= b[0]) { return [a[0]].concat(merge(a.slice(1, a.length), b)); }
	if (b[0] <= a[0]) { return [b[0]].concat(merge(a, b.slice(1, b.length))); }

}

function mergeSort(array) {
	if (array.length === 1) { return array;	}
	var halfLength = array.length / 2;
	var a = mergeSort(array.slice(0, halfLength));
	var b = mergeSort(array.slice(halfLength, array.length));
	return merge(a, b);
}

var sortMe = [5, 8, 3, 9, 23, 55, 10, 7];