import React from 'react';
import Alert from 'react-bootstrap/Alert';
import './Err-Load.css';

function Success({message}) {
  return (
    <div className="success-con">
    <Alert variant="success">
    <Alert.Heading>{message}</Alert.Heading>
    </Alert>
</div>
  )
}

export default Success