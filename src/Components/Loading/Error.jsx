import React from 'react';
import Alert from 'react-bootstrap/Alert';
import './Err-Load.css';

function Error() {
  return (
    <div className="err-con">
        <Alert variant="danger">
      <Alert.Heading>Error,Something Seems to be Wrong,Kindly Reload</Alert.Heading>
    </Alert>
    </div>
  )
}

export default Error