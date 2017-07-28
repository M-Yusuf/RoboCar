
function poster() {
  $.ajax({
    type: "POST",
    url: "/ajax",
    data: JSON.stringify({ direction: "forward" }),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
  });
}