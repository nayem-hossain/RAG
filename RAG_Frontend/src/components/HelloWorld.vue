<script setup>
import { ref, unref } from 'vue';

const question = ref('');
const response = ref('');
const resultData = ref('');

const fetchResponse = async () => {
  try {
    console.log(unref(question)); // Log the question value
    const res = await fetch('http://0.0.0.0:8000/query', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: unref(question) }),
    });
    console.log('Response object:', res); // Log the Response object

    if (!res.ok) {
      throw new Error(`HTTP error ${res.status}`);
    }

    const data = await res.json();
    console.log('Response data:', data[0]); // Log the response data
    resultData.value = data[0].response; // Assign the response text to the resultData ref
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};
</script>

<template>
  <v-container class="d-flex justify-center align-center fill-height" fluid>
    <div>
      <div class="image mb-4">
        <v-img :width="300" aspect-ratio="16/9" cover src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"></v-img>
      </div>
      <v-textarea v-model="question" label="Enter your question" variant="outlined"></v-textarea>
      <v-btn @click="fetchResponse"> Ask </v-btn>
      <div class="result-container">
        <v-textarea v-model="resultData" label="Response" variant="outlined" readonly></v-textarea>
      </div>
    </div>
  </v-container>
</template>

<style scoped>
.fill-height {
  height: 100vh;
}
.image {
  margin-top: 200px;
  margin-bottom: 20px;
}
.result-container {
  margin-top: 20px; /* Add some spacing between the button and the result area */
}
</style>