(function ($) {
    $(document).ready(function () {
        var table = $('#customers_id').DataTable({
            paging: true,
            pageLength: 10,
            ordering: true,
            bProcessing: false,
            columnDefs: [{
                targets: -1,
                orderable: false
            }],
            buttons: [
            'pdfHtml5',
            'excelHtml5' 
        ]
        });
        // Initialize filterTable plugin
        table.filterTable('#contact-filter');
    });
})(jQuery);




var counter = 1;

function addProductField() {
    var material_obj = $('#material_obj').val()
    var material_list = JSON.parse(material_obj);
    var container = document.getElementById("dynamicFieldsContainer");
    var newRow = document.createElement("div");
    newRow.className = "row mt-3";

    var materialId = "material_id_" + counter;
    var materialPercentage = "material_percentage_" + counter;

    newRow.innerHTML = `
        <div class="col-lg-4">
            <label>Material Name</label>
            <select class="form-control typeable-select2" id="${materialId}" name="${materialId}">
                <option class="bg-info">Select Material </option>

            </select>
        </div>
        <div class="col-lg-4">
            <label>Material Percentage</label>
            <div class="d-flex">
                <input type="text" class="form-control" id="${materialPercentage}" name="${materialPercentage}" placeholder="Please enter material percentage" value="">
            </div>
        </div>
        <div class="col-lg-4">
            <label></label>
            <div class="d-flex">
                <button class="btn btn-sm btn-danger mt-3" onclick="removeProductField(this)">Remove</button>
                <button class="btn btn-sm btn-primary float-right mt-3" onclick="addProductField()"> +Add</button>
            </div>
        </div>
    `;

    container.appendChild(newRow);

    var selectElement = document.getElementById(materialId);
    material_list.forEach(function(material) {
        var option = document.createElement("option");
        option.text = material.fields.MaterialName;
        option.value = material.pk;
        selectElement.appendChild(option);
    });


    $(`#${materialId}`).select2({
        placeholder: "Select Material",
        theme: "bootstrap5",
        width: "100%" 
    });

    counter++;
}




function removeProductField(button) {
    var rowToRemove = button.parentNode.parentNode.parentNode;
    rowToRemove.remove();
}


function addDynamicField() {
    // Clone the existing field container
    var container = document.getElementById('dynamicFieldsContainer');
    var newContainer = container.cloneNode(true);

    // Clear input values in the cloned container
    var inputs = newContainer.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].value = '';
    }

    // Append the cloned container to the parent
    container.parentNode.appendChild(newContainer);
}