<script setup lang="ts">
  import { Authenticator } from "@aws-amplify/ui-vue";

  import { Amplify } from 'aws-amplify';
  import awsconfig from '../aws-exports';

  Amplify.configure(awsconfig);
</script>

<template>
    <authenticator>
      <template v-slot:sign-up-header>
        <h3
          class="amplify-heading"
          style="padding: var(--amplify-space-xl) 0 0 var(--amplify-space-xl)"
        >
          Create a new account
        </h3>
      </template>
      <template v-slot:header>
        <div style="padding: var(--amplify-space-large); text-align: center">
          <img
            class="amplify-image"
            alt="Amplify logo"
            src="../assets/balanceada.png"
          />
        </div>
      </template>
      <template v-slot:sign-in-header>
        <h3
          class="amplify-heading"
          style="padding: var(--amplify-space-xl) 0 0 var(--amplify-space-xl)"
        >
          Sign in to your account
        </h3>
      </template>
      <template v-slot="{ user, signOut }">
        {{ user }}
        <h1>Hello {{ user.username }}!</h1>
        <button @click="signOut" variation="primary">Sign Out</button>
      </template>
      <template v-slot:footer>
        <div style="padding: var(--amplify-space-large); text-align: center">
          <p class="amplify-text" style="color: var(--amplify-colors-neutral-80)">
            © All Rights Reserved
          </p>
        </div>
      </template>
    </authenticator>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
:root {
    --amplify-colors-brand-secondary-90: #E57212;
}
[data-amplify-authenticator] {
  --amplify-components-button-primary-background-color: var(
    --amplify-colors-brand-secondary-80
  );
  --amplify-components-button-primary-hover-background-color: var(
    --amplify-colors-brand-secondary-90
  );
  --amplify-components-button-primary-focus-background-color: var(
    --amplify-colors-brand-secondary-90
  );
  --amplify-components-button-primary-active-background-color: var(
    --amplify-colors-brand-secondary-100
  );
  --amplify-components-button-link-color: var(
    --amplify-colors-brand-secondary-80
  );
  --amplify-components-button-link-hover-color: var(
    --amplify-colors-brand-secondary-90
  );
  --amplify-components-button-link-focus-color: var(
    --amplify-colors-brand-secondary-90
  );
  --amplify-components-button-link-active-color: var(
    --amplify-colors-brand-secondary-100
  );
  --amplify-components-button-link-active-background-color: transparent;
  --amplify-components-button-link-focus-background-color: transparent;
  --amplify-components-button-link-hover-background-color: transparent;
}
</style>