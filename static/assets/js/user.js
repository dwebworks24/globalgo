

function reset(){
    $("#Username").val('')
    $("#email").val('')
    $("#password").val('')
    $("#confirm_password").val('')
    $("#phone").val('')
}

function creatuser(){
    const countery_name = $("#countery_name").val()
    const visa_type = $("#visa_type").val()
    const username = $("#username").val()
    const phone = $("#phonenumber").val()
    const emailId = $("#email").val()
    const password = $("#password").val()
    const confirm_password = $("#confirm_password").val()
    
    var formData = new FormData()
    formData.append('countery_name', countery_name)
    formData.append('visa_type', visa_type)
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



function add_depented() {

    const dependentsContainer = document.getElementById('dependents-container');

    const newDependent = document.createElement('div');
    newDependent.classList.add('row', 'dependent-row');
    newDependent.innerHTML = `
    <h4 class="font-normal mt-2 text-warning">Dependent Details</h4>
            <div class="col-md-4 col-sm-12 col-xs-12">
                <label for="dependent_first_name">First Name</label>
                <input type="text" id="dependent_first_name" name="dependent_first_name[]" class="form-control"
                    placeholder="Please enter first name" required data-error="Please enter your first name">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12">
                <label for="dependent_last_name">Last Name</label>
                <input type="text" id="dependent_last_name" name="dependent_last_name[]" class="form-control"
                    placeholder="Please enter last name" required data-error="Please enter your last name">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12">
                <label for="dependent_email">Email</label>
                <input type="email" id="dependent_email" name="dependent_email[]" class="form-control"
                    placeholder="Please enter email" required data-error="Please enter your email">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12 mt-3">
                <label for="dependent_phone_number">Phone Number</label>
                <input type="text" id="dependent_phone_number" name="dependent_phone_number[]" class="form-control"
                    placeholder="Please enter phone number" required data-error="Please enter your phone number">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12 mt-3">
                <label for="dependent_second_phone_number">Second Phone Number (optional)</label>
                <input type="text" id="dependent_second_phone_number" name="dependent_second_phone_number[]" class="form-control"
                    placeholder="Please enter second phone number">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12 mt-3">
                <label for="dependent_passport_front">Upload Passport Front</label>
                <input type="file" id="dependent_passport_front" name="dependent_passport_front[]" class="form-control"
                    required data-error="Please upload passport front">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12 mt-3">
                <label for="dependent_passport_back">Upload Passport Back</label>
                <input type="file" id="dependent_passport_back" name="dependent_passport_back[]" class="form-control"
                    required data-error="Please upload passport back">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12 mt-3">
                <label for="dependent_aadhar_front">Upload Aadhar Front</label>
                <input type="file" id="dependent_aadhar_front" name="dependent_aadhar_front[]" class="form-control"
                    required data-error="Please upload Aadhar front">
            </div>
            <div class="col-md-4 col-sm-12 col-xs-12 mt-3">
                <label for="dependent_aadhar_back">Upload Aadhar Back</label>
                <input type="file" id="dependent_aadhar_back" name="dependent_aadhar_back[]" class="form-control"
                    required data-error="Please upload Aadhar back">
            </div>
            <div class="col-md-12 col-sm-12 col-xs-12 mt-3">
            <button class="btn btn-danger btn-sm" type="button" onclick="removeDependent(this)">- Remove Dependent</button>
        </div>
        `;

    dependentsContainer.appendChild(newDependent);
}

function removeDependent(button) {
    const dependentRow = button.closest('.dependent-row');
    dependentRow.remove();
}







// step3
function showOrganizationDetails() {
    document.getElementById('organization_details').classList.remove('d-none');
}

function hideOrganizationDetails() {
    document.getElementById('organization_details').classList.add('d-none');
}

// save form #######################################  STEP1 ################
function save_customer_info(){
    
    let formData = new FormData();

        // Get form values and files
    const customer_id = $('#customer_id').val();
    const first_name = $('#first_name').val();
    const last_name = $('#last_name').val();
    const email = $('#email').val();
    const phone_number = $('#phone_number').val();
    const second_phone_number = $('#second_phone_number').val();

    const passport_front = $('#passport_front')[0].files[0];
    const passport_back = $('#passport_back')[0].files[0];
    const aadhar_front = $('#aadhar_front')[0].files[0];
    const aadhar_back = $('#aadhar_back')[0].files[0];

        // Append values to formData
    formData.append('customer_id', customer_id);
    formData.append('first_name', first_name);
    formData.append('last_name', last_name);
    formData.append('email', email);
    formData.append('phone_number', phone_number);
    formData.append('second_phone_number', second_phone_number);

    formData.append('passport_front', passport_front);
    formData.append('passport_back', passport_back);
    formData.append('aadhar_front', aadhar_front);
    formData.append('aadhar_back', aadhar_back);

    $.ajax({
        url: '/add_user_info/',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
            show_success(response['message'])
        
        },
        error: function(xhr, status, error) {
            show_error(response.responseJSON['message'])
        }
    });
}
// save form #######################################  STEP2 ################

function saveDependents() {
    const form = document.getElementById('userAccountSetupForm');
    const formData = new FormData(form);

    const dependentsData = [];
    const firstNames = formData.getAll('dependent_first_name[]');
    const lastNames = formData.getAll('dependent_last_name[]');
    const emails = formData.getAll('dependent_email[]');
    const phoneNumbers = formData.getAll('dependent_phone_number[]');
    const secondPhoneNumbers = formData.getAll('dependent_second_phone_number[]');
    const passportFronts = formData.getAll('dependent_passport_front[]');
    const passportBacks = formData.getAll('dependent_passport_back[]');
    const aadharFronts = formData.getAll('dependent_aadhar_front[]');
    const aadharBacks = formData.getAll('dependent_aadhar_back[]');

    for (let i = 0; i < firstNames.length; i++) {
        dependentsData.push({
            firstName: firstNames[i],
            lastName: lastNames[i],
            email: emails[i],
            phoneNumber: phoneNumbers[i],
            secondPhoneNumber: secondPhoneNumbers[i],
            passportFront: passportFronts[i],
            passportBack: passportBacks[i],
            aadharFront: aadharFronts[i],
            aadharBack: aadharBacks[i]
        });
    }
    formData.append('dependents', JSON.stringify(dependentsData));
    $.ajax({
        url: '/add_dependent_info/',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
            show_success(response['message'])
        
        },
        error: function(xhr, status, error) {
            show_error(response.responseJSON['message'])
        }
    })
}



// save form #######################################  STEP 3 ################

function save_UsPoint_of_contact() {
    const customer_id = $('#customer_id').val();
    var first_name = $("#us_point_first_name").val();
    var last_name = $("#us_point_last_name").val();
    // var experience_type = $("#us_point_experience_type").val();
    var years_experience = parseInt($("#us_point_years_experience").val());
    var organization_yes_no = $("input[name='us_point_organization_yes_no']:checked").val();
    var organization_name = $("#us_point_organization_name").val();
    var organization_address = $("#us_point_organization_address").val();
    var relationship_to_you = $("#us_point_relationship_to_you").val();
    var us_street_name = $("#us_point_us_street_name").val();
    var us_street_address = $("#us_point_us_street_address").val();
    var city = $("#us_point_city").val();
    var state = $("#us_point_state").val();
    var zipcode = $("#us_point_zipcode").val();
    var phone = $("#us_point_phone").val();
    var email = $("#us_point_email").val();

    var formData = new FormData();
    formData.append('customer_id', customer_id);
    formData.append('first_name', first_name);
    formData.append('last_name', last_name);
    // formData.append('experience_type', experience_type);
    formData.append('years_experience', years_experience);
    formData.append('organization_yes_no', organization_yes_no);
    formData.append('organization_name', organization_name);
    formData.append('organization_address', organization_address);
    formData.append('relationship_to_you', relationship_to_you);
    formData.append('us_street_name', us_street_name);
    formData.append('us_street_address', us_street_address);
    formData.append('city', city);
    formData.append('state', state);
    formData.append('zipcode', zipcode);
    formData.append('phone', phone);
    formData.append('email', email);


    $.ajax({
        url: '/us_point_of_contact/',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
            show_success(response['message'])
        
        },
        error: function(xhr, status, error) {
            show_error(response.responseJSON['message'])
        }
    })
   
}

function save_cgi_application(){
    const customer_id = $('#customer_id').val();
    var username = $("#username").val();
    var password = $("#password").val();
    var security_question_1 = $("#security_question_1").val();
    var security_answer_1 = $("#security_answer_1").val();
    var security_question_2 = $("#security_question_2").val();
    var security_answer_2 = $("#security_answer_2").val();
    var security_question_3 = $("#security_question_3").val();
    var security_answer_3 = $("#security_answer_3").val();  
    
    var formData = new FormData();
    formData.append('customer_id', customer_id);
    formData.append('username', username);
    formData.append('password', password);
    formData.append('security_question_1', security_question_1);
    formData.append('security_answer_1', security_answer_1);
    formData.append('security_question_2', security_question_2);
    formData.append('security_answer_2', security_answer_2);
    formData.append('security_question_3', security_question_3);
    formData.append('security_answer_3', security_answer_3);

    $.ajax({
        url: '/cgi_application/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            show_success(response['message'])
        },
        error: function(xhr, status, error) {
            show_error(response.responseJSON['message'])
        }
    });
}




function save_ceac_application(){
    const customer_id = $('#customer_id').val();
    var username = $("#ceac_username").val();
    var password = $("#ceac_password").val();
    var question = $("#ceac_question1").val();
    var answer = $("#ceac_security_answer_1").val();
   
    
    var formData = new FormData();
    formData.append('customer_id', customer_id);
    formData.append('username', username);
    formData.append('password', password);
    formData.append('question', question);
    formData.append('answer', answer);


    $.ajax({
        url: '/ceac_application/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            show_success(response['message'])
        },
        error: function(xhr, status, error) {
            show_error(response.responseJSON['message'])
        }
    });
}



function save_contact(){
    var firstName = $("#firstName").val();
    var conEmail = $("#conEmail").val();
    var phone = $("#conPhone").val();
    var subject = $("#conSubject").val();
    var message = $("#conMessage").val();

    var formData = {
        firstName: firstName,
        conEmail: conEmail,
        conPhone: phone,
        conSubject: subject,
        conMessage: message,
    };

    $.ajax({
        type: 'POST',
        url: '/contact_submit/',  
        data: formData,
        success: function(response) {
            show_success(response['message'])
        },
        error: function(xhr, status, error) {
            show_error(response.responseJSON['message'])
        }
    });
}