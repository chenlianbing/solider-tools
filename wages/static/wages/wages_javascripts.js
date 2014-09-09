

/*
Purpose: Wage Calculation, include validation check
Added:   2014年9月9日17:00:29
*/
function calculateWage() {
	var inputSales, err_message;
	var sum = 0.0;
	
	err_message = document.getElementById("err_message");
	err_message.innerHTML = ""
	
	inputSales = document.getElementById("sales").value;
	try {
		if (inputSales == "") {
			throw "输入为空，请重新输入。"		
		}
		else if (isNaN(inputSales)) {
			throw "不是有效数字。";
		} else if (inputSales < 0) {
			throw "销售额不能为负。";
		} else if (inputSales >= Number.MAX_VALUE) {
			throw "数字超过最大值，请核对后输入。"
		} else {
			sum = calcPercentageDeduct(inputSales);
			document.getElementById("sales").value = "";
			document.getElementById("demo").innerHTML = sum;
		}	
	}
	catch (err)	{
		err_message.innerHTML = "输入错误：" + err;
	} 
}

/*
Purpose: According input sales, calculate the percentage deduct.
Added:   2014年9月9日17:01:04
*/

function calcPercentageDeduct(sales) {
	
	var percentageSalesArray = [0, 60000, 110000, 160000, 200000, 240000, 280000, 310000, 340000];
	var percentageDeductArray = [
								 Number(wageCalcPercentageDeduct0W),
								 Number(wageCalcPercentageDeduct6W),
								 Number(wageCalcPercentageDeduct11W),
								 Number(wageCalcPercentageDeduct16W),
								 Number(wageCalcPercentageDeduct20W),
								 Number(wageCalcPercentageDeduct24W),
								 Number(wageCalcPercentageDeduct28W),
								 Number(wageCalcPercentageDeduct31W),
								 Number(wageCalcPercentageDeduct34W)];
								 	
	var anchorIndex = 0;
	var sum = 0;
	
	for (i=percentageSalesArray.length; i>=0; i-- ) {
		if (sales > percentageSalesArray[i]) {
			anchorIndex = i;
			break;
		}
	}
	
	sum = (sales - percentageSalesArray[anchorIndex]) * percentageDeductArray[anchorIndex];
	for (i=anchorIndex; i>0; i--) {
		sum += ((percentageSalesArray[i] - percentageSalesArray[i-1]) * percentageDeductArray[i-1])
	}
	
	return sum;
}
