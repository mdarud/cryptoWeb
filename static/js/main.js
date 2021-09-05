$(document).ready(function () {
  $(".nav-tabs a").click(function () {
    $(this).tab("show");
  });
});

$(".custom-file-input").on("change", function () {
  var fileName = $(this).val().split("\\").pop();
  $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

$("#encrypt").click(function() {
  $(this).closest("form").attr("action", "/encrypt");     
});
$("#decrypt").click(function() {
  $(this).closest("form").attr("action", "/decrypt");       
});

$("#encryptFile").click(function() {
  $(this).closest("form").attr("action", "/encrypt-file");     
});
$("#decryptFile").click(function() {
  $(this).closest("form").attr("action", "/decrypt-file");       
});

$('.method-select-text').on('change', function() {
  if (this.value == "affine"){
    $('.text-input').html('<div class="col-md-6 form-group mb-3"><label for="" class="col-form-label">Text</label> <input type="text" class="form-control" name="text" id="text" placeholder="Insert text" required/> </div> <div class="col-md-3 form-group mb-3"> <label for="" class="col-form-label">Key a</label> <input type="number" class="form-control" name="keyA" id="keyA" placeholder="Insert key a" required/></div><div class="col-md-3 form-group mb-3"> <label for="" class="col-form-label">Key b</label> <input type="number" class="form-control" name="keyB" id="keyB" placeholder="Insert key b" required/></div>');
  } else {
    $('.text-input').html('<div class="col-md-6 form-group mb-3"><label for="" class="col-form-label">Text</label> <input type="text" class="form-control" name="text" id="text" placeholder="Insert text" required/> </div> <div class="col-md-6 form-group mb-3"> <label for="" class="col-form-label">Key</label> <input type="text" class="form-control" name="key" id="key" placeholder="Insert key" required/></div>');
  }
});

$('.file-select').change(function() {
  if (this.value == "binary"){
    $('.custom-file-input').removeAttr("accept");
    $('.method-select-file').val("exvigenere")
    $('.method-select-file').attr("disabled",true);
  } else {
    $('.method-select-file').removeAttr("disabled");
    $('.custom-file-input').attr("accept", "text/plain");
  }
})

$('.method-select-file').on('change', function() {
  if (this.value == "affine"){
    $('.file-input').html('<div class="col-md-6 form-group mb-3"><label for="" class="col-form-label">Key a</label> <input type="number" class="form-control" name="keyA" id="keyA" placeholder="Insert key a"/></div><div class="col-md-6 form-group mb-3"><label for="" class="col-form-label">Key b</label> <input type="number" class="form-control" name="keyB" id="keyB" placeholder="Insert key b"/></div>');
  } else {
    $('.file-input').html('<div class="col-md-12 form-group mb-3"><label for="" class="col-form-label">Key</label> <input type="text" class="form-control" name="key" id="key" placeholder="Insert key"/></div>');
  }
});
