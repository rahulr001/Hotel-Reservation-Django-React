import React,{useState} from 'react';
import HashLoader from "react-spinners/HashLoader";
import './Err-Load.css'

function Loading() {
    
      let [loading, setLoading] = useState(true);
     
  return (
    <div className="sweet-loading">
      <HashLoader
        color='#FFB100'
        loading={loading}
        css=''
        size={80}
        // aria-label="Loading Spinner"
        // data-testid="loader"
      />
    </div>
  )
}

export default Loading;