

function reset(){
    $("#Username").val('')
    $("#email").val('')
    $("#password").val('')
    $("#confirm_password").val('')
    $("#phone").val('')
}

function creatuser(){
    const username = $("#username").val()
    const phone = $("#phonenumber").val()
    const emailId = $("#email").val()
    const password = $("#password").val()
    const confirm_password = $("#confirm_password").val()
    
    var formData = new FormData()
    formData.append('username', username)
    formData.append('phone', phone)
    formData.append('emailId', emailId)
    formData.append('password', password)
    formData.append('confirm_password', confirm_password)

    $.ajax({
        url: '/user_register/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            userid = response['user_id']
            window.location.href = '/visa_application/' + userid + '/';
            reset()
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}






function creatstaff(){
    const username = $("#username").val()
    const phone = $("#phonenumber").val()
    const emailId = $("#email").val()
    const password = $("#password").val()
    const confirm_password = $("#confirm_password").val()
    
    var formData = new FormData()
    formData.append('username', username)
    formData.append('phone', phone)
    formData.append('emailId', emailId)
    formData.append('password', password)
    formData.append('confirm_password', confirm_password)

    $.ajax({
        url: '/staff_register/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
            reset()
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}


function updateProfile(){
    const userid = $("#user_id").val();
    const firstname = $("#first_name").val();
    const lastname = $("#last_name").val();
    const referal_code = $("#referal_code").val();
    const dateofbirth = $("#date_of_birth").val();
    const address = $("#address").val();
    const pincode = $("#pincode").val();
    const image = $("#profile_image")[0].files[0];
    const username = $("#username").val();
    const phone = $("#phone").val();
    const emailId = $("#email").val();

    var formData = new FormData();
    formData.append('userid', userid);
    formData.append('username', username);
    formData.append('phone', phone);
    formData.append('emailId', emailId);
    formData.append('firstname', firstname);
    formData.append('lastname', lastname);
    formData.append('referal_code', referal_code);
    formData.append('dateofbirth', dateofbirth);
    formData.append('address', address);
    formData.append('pincode', pincode);
    formData.append('image', image);
   
   

    $.ajax({
        url: '/updateprofile/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
            // reset()
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}


function reset(){
    $("#Username").val('')
    $("#email").val('')
    $("#password").val('')
    $("#confirm_password").val('')
    $("#phone").val('')
}


function resetlogin() {
    $("#email").val('');
    $("#password").val('');
}


function userlogin(){
    const email = $("#email").val()
    const password = $("#password").val()
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
    
    var formData = new FormData()
    formData.append('emailId', email)
    formData.append('password', password)
    formData.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
   
    $.ajax({
        url: '/sigin/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            if (response.redirect_url) {
                resetlogin();
                window.location.href = response.redirect_url;
            } else {
                
            }
            
            
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}



function verifyotp(){
    const getotp = $("#otp").val()

    var formData = new FormData()
    formData.append('enterOtp', getotp)
    
   
    $.ajax({
        url: '/otp_verification/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            if (response) {
                window.location.href = '/change_password/';
            } else {
                alert("fail to redirect")
            }
            
            
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}

function verifaccount(){
    const getemail = $("#email_id").val()

    var formData = new FormData()
    formData.append('email', getemail)
    
   
    $.ajax({
        url: '/reset_password_link/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}



function changePassword(){
    const old_password = $("#old_password").val()
    const new_password = $("#new_password").val()
    const confirm_password = $("#confirm_password").val()

    var formData = new FormData()
    formData.append('oldPassword', old_password)
    formData.append('newPassword', new_password)
    formData.append('confirmPassword', confirm_password)
    
   
    $.ajax({
        url: '/change_user_password/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}

function userResertPassword(){
    const new_password = $("#new_password").val()
    const confirm_password = $("#confirm_password").val()

    var formData = new FormData()
    formData.append('newPassword', new_password)
    formData.append('confirmPassword', confirm_password)
    
    $.ajax({
        url: '/passwordReset/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
        },
        error: function(response){
            // show_error(response.responseJSON['message'])
        }
        
    })
}

const navigateToFormStep = (stepNumber) => {
	document.querySelectorAll(".form-step").forEach((formStepElement) => {
		formStepElement.classList.add("d-none");
	});
	document.querySelectorAll(".form-stepper-list").forEach((formStepHeader) => {
		formStepHeader.classList.add("form-stepper-unfinished");
		formStepHeader.classList.remove("form-stepper-active", "form-stepper-completed");
	});
	document.querySelector("#step-" + stepNumber).classList.remove("d-none");
	const formStepCircle = document.querySelector('li[step="' + stepNumber + '"]');
	formStepCircle.classList.remove("form-stepper-unfinished", "form-stepper-completed");
	formStepCircle.classList.add("form-stepper-active");
	for (let index = 0; index < stepNumber; index++) {
		const formStepCircle = document.querySelector('li[step="' + index + '"]');
		if (formStepCircle) {
			formStepCircle.classList.remove("form-stepper-unfinished", "form-stepper-active");
			formStepCircle.classList.add("form-stepper-completed");
		}
	}
};
document.querySelectorAll(".btn-navigate-form-step").forEach((formNavigationBtn) => {
	formNavigationBtn.addEventListener("click", () => {
		const stepNumber = parseInt(formNavigationBtn.getAttribute("step_number"));
		navigateToFormStep(stepNumber);
	});
});


$(document).ready(function() {
    $('#visa-applications-table').DataTable({
        buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
        
    }
    );
    
});