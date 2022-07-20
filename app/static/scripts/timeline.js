  const form = document.getElementById('timeline-form');
  form.addEventListener('submit', function(e) {
    e.preventDefault(); // prevent default behaviour

    const prePayload = new FormData(form);
    const payload = new URLSearchParams(prePayload); // convert object to URL-endoded string

    console.log([...payload])

    fetch('/api/timeline_post', { //using fetch, post to endpoint
      method: "POST",
      body: payload,
    })
    .then(res => {
      if (res.status == 400) {
        res.text().then(errorMessage => alert(errorMessage))
      } else if (res.status == 429) {
        res.text().then(alert("You have reached the rate limit. 1 post per minute."))
      } else {
        return res.json()
      }
    }) // server response, convert to javascript object
    .then(data => {
    console.log(data)
    form.reset(); // form reset
    location.reload() // reload page to display new data
    })
    .catch(err => console.log(err));
  })

  function deletepost(post_id) {
    console.log("here is post_id" + post_id)
    fetch('/api/timeline_post/' + post_id, {
      method: "DELETE",
    })
    .then(() => {
    location.reload(); // reload page to display new data
    })
    .catch(err => console.log(err));
  }