var drawShape = function(x, y, radius,colorNum) {

    fill(5 * colorNum, 3 * colorNum, 2* colorNum);
    ellipse(x, y, radius, radius);
    
    if (radius >= 2) {
        drawShape(x/1.042, y*1.020, radius/1.225, colorNum* 1.14);
    }
};

drawShape(width/2, height/2, 391,23);

