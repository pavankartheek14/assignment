import React from 'react'

export default function Text() {
    const [formData, setFormData] = React.useState({
        modelName: '',
        domain: ''
      });
    
      const handleOnchange = (e) => {
        setFormData({
          ...formData,
          [e.target.name]: e.target.value
        });
      };

    const [storedData,setStoredData]=React.useState([]);
    const handlesubmit=()=>{
        setStoredData([...storedData, formData]);
        setFormData({
            modelName: '',
            domain: ''
        });
        
    }
  return (
    <div>
      <div className="container" >
            <h2>Enter the Model Name </h2>
                <div className="mb-3">
                    <textarea className="form-control" name="modelName" value={formData.modelName} onChange={handleOnchange}  id="myBox" rows="2"></textarea>
                </div>
            <h2> Enter the domain</h2>
                < div className="mb-3">
                    <textarea className="form-control" name="domain" value={formData.domain} onChange={handleOnchange}  id="myBox" rows="2"></textarea>
                </div>
                <button className="btn btn-primary " onClick={handlesubmit}>submit</button>
                
            </div>
            <div className='container' >
                <h2>Entered data:</h2>
                {storedData.length === 0 ? (
          <p>No submissions yet.</p>
        ) : (
          <ul className="list-group">
            {storedData.map((item, index) => (
              <li key={index} className="list-group-item">
                Model: {item.modelName} <br />
                Domain: {item.domain}
              </li>
            ))}
          </ul>
        )}
    
            </div>   
    </div>
  )
}
