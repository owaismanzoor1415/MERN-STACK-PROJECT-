import React, { useEffect, useState } from 'react'
import Hero from '../Components/Hero/Hero'
import Popular from '../Components/Popular/Popular'
import Offers from '../Components/Offers/Offers'
import NewCollections from '../Components/NewCollections/NewCollections'
import NewsLetter from '../Components/NewsLetter/NewsLetter'

const Shop = () => {

  const [popular, setPopular] = useState([]);
  const [newcollection, setNewCollection] = useState([]);

  
    useEffect(() => {
      const fetchInfo = async () => {
        try {
          const popularResponse = await fetch('http://localhost:4000/popularinwomen');
          if (!popularResponse.ok) {
            throw new Error(`Failed to fetch popularinwomen: ${popularResponse.status} ${popularResponse.statusText}`);
          }
          const popularData = await popularResponse.json();
          setPopular(popularData);
      
          const newCollectionResponse = await fetch('http://localhost:4000/newcollections');
          if (!newCollectionResponse.ok) {
            throw new Error(`Failed to fetch newcollections: ${newCollectionResponse.status} ${newCollectionResponse.statusText}`);
          }
          const newCollectionData = await newCollectionResponse.json();
          setNewCollection(newCollectionData);
      
        } catch (error) {
          console.error('Error fetching data:', error.message);
          // Handle the error accordingly, e.g., display an error message to the user
        }
      };
      
    
      fetchInfo();
    }, [])


  return (
    <div>
      <Hero/>
      <Popular data={popular}/>
      <Offers/>
      <NewCollections data={newcollection}/>
      <NewsLetter/>
    </div>
  )
}

export default Shop
