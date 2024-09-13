
function SendEmailButton({ userId, guideId }) {
  const sendEmail = () => {
    fetch('/send_email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_id: userId,
        guide_id: guideId,
      }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          alert('Failed to send email: ' + data.error);
        } else {
          alert('Email sent!');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  return (
    <button onClick={sendEmail}>Send Guide Email</button>
  );
}

export default SendEmailButton;