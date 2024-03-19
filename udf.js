function transform(line) {
    if (line.startsWith("id")) { // Assuming "id" is the first column name
        return null; // Skip the line
    }
    var values = line.split(',');
    var obj = new Object();
    obj.id = values[0];
    obj.rank = values[1];
    obj.name = values[2];
    obj.country = values[3];
    obj.rating = values[4];
    obj.trend = values[5];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}
