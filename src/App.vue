<template>
  <div id="app">
    <!-- Conditionally render AuthenticatorComponent if user is not authenticated -->
    <AuthenticatorComponent v-if="!isAuthenticated" />
    <div v-else>
      <!-- Your app's content for authenticated users goes here -->
      <h1>Welcome, {{ username }}!</h1>
      <button @click="signOutUser">Sign Out</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getCurrentUser, signOut } from 'aws-amplify/auth';

import AuthenticatorComponent from './components/AuthenticatorComponent.vue';

// State to track if user is authenticated
const isAuthenticated = ref(false);
const user = ref(null);
const username = ref("");

onMounted(async () => {
  try {
    const userInfo = await getCurrentUser();
    username.value = userInfo.username

    console.log(`The username: ${userInfo.username}`);
    console.log(`The userId: ${userInfo.userId}`);
    console.log(`The signInDetails: ${userInfo.signInDetails}`);
    isAuthenticated.value = true;

    if(!userInfo)
      user.value = userInfo;
  } catch (error) {
    console.log('User is not authenticated:', error);
    isAuthenticated.value = false;
  }
});

// Sign out method
const signOutUser = async () => {
  try {
    await signOut();
    isAuthenticated.value = false;
    user.value = null;
  } catch (error) {
    console.error('Error signing out: ', error);
  }
};
</script>
