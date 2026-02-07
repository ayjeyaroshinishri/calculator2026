<!DOCTYPE html>
<html>
<head>
    <title>Calculator 2026</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: #f4f4f4;
        }
        .box {
            margin: 50px auto;
            width: 300px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 0 10px gray;
        }
        input, select, button {
            margin: 8px;
            padding: 8px;
            width: 90%;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>Calculator Menu</h2>

    <input type="number" id="num1" placeholder="Enter first number">
    <input type="number" id="num2" placeholder="Enter second number">

    <select id="operation">
        <option value="add">Addition</option>
        <option value="sub">Subtraction</option>
        <option value="mul">Multiplication</option>
        <option value="div">Division</option>
        <option value="mod">Modulus</option>
    </select>

    <button onclick="calculate()">Calculate</button>

    <h3 id="result"></h3>
</div>

<script>
function calculate() {
    let a = parseFloat(document.getElementById("num1").value);
    let b = parseFloat(document.getElementById("num2").value);
    let op = document.getElementById("operation").value;
    let res;

    if (isNaN(a) || isNaN(b)) {
        document.getElementById("result").innerText = "Enter valid numbers!";
        return;
    }

    switch(op) {
        case "add":
            res = a + b;
            break;
        case "sub":
            res = a - b;
            break;
        case "mul":
            res = a * b;
            break;
        case "div":
            if (b === 0) {
                res = "Cannot divide by zero";
            } else {
                res = a / b;
            }
            break;
        case "mod":
            res = a % b;
            break;
    }

    document.getElementById("result").innerText = "Result: " + res;
}
</script>

</body>
</html>
